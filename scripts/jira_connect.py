import csv
import json
import re
import os
from os import path
from atlassian import Jira
import logging
import logging.config
import argparse
import textwrap
from dotenv import load_dotenv
from JiraIssue import JiraIssue


# fmt: off
CONFIG = '''
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(asctime)s || %(process)d :: %(levelname)s :: %(message)s"
        }
    },
    "filters": {
        "warnings_and_below": {
            "()" : "__main__.filter_maker",
            "level": "WARNING"
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
            "filters": ["warnings_and_below"]
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stderr"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "debug.log",
            "mode": "w"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "stderr",
            "stdout",
            "file"
        ]
    }
}
'''

DESCRIPTION = """

                GRIT-realtime
-------------------------------------------------
            The Mis-nomer that stuck
-------------------------------------------------
            By DLBPointon (dp24)
-------------------------------------------------
GRIT-realtime is the project born out of a need
to collect pre/post curation summary statistics.

Created during my BSc Bioinformatics apprentice-
ship and continually developed afterwards, this
full stack project uses:
- Docker-compose
- PostgreSQL
- PostgREST
- Static HTML site
- Python3
    - for data retrieval and manipulation
- Javascript
    - for DB calling and plot generation

V1-2 - RShiny
V3-5 - Roughly followed the current set up
V6   - Current Version is a rewrite of V5
     - Utilising a Class structure for the
     jira data. Data is also written
     immediately, much more efficient
     also still pretty slow due to limits
     caused by the Jira system.
     - Also had to change the Jira python library
     to atlassian-python-api because Atlassian?
     New one is better, but they should really
     document that the API has a 1000 ticket
     hardlimit.
     - Because of the above, Pagination!
     Now gets all data rather than just the first
     970 (-30 tickets that get thrown out).

"""

VERSION = "6.0.0"

def parse_args():
    parser = argparse.ArgumentParser(
        prog="GRIT-realtime",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(DESCRIPTION),
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Where to chuck the output?", default="../grit-boot/output/jira_dump.tsv"
    )
    parser.add_argument(
        "-l", "--hardlimit", type=int, help="Hardlimit for Jira. MAX is 1000.", default=800
    )
    parser.add_argument("-v", "--version", action="version", version=VERSION)

    return parser.parse_args()


def dotloader():
    load_dotenv("../.env")
    jira_user = os.getenv("JIRA_USER")
    jira_pass = os.getenv("JIRA_PASS")
    jira_token = os.getenv("JIRA_TOKEN")
    return jira_user, jira_pass, jira_token


def get_list_of_pages(limit: int, max_results: int):
    start = 0
    index_list = []
    while limit < max_results:

        index_list.append([start, limit, limit])
        start += limit + 1
        limit += limit
        if limit > max_results:
            index_list.append([start - 801, max_results, limit])

    return index_list


def get_pages(hard_limit, limit_list, jira_jql, jira):
    return jira.jql(
        jql=jira_jql,
        start=limit_list[0],
        limit=hard_limit,
    )


def prep_folder(location):
    directory = "/".join(location.split("/")[:-1])
    os.makedirs(directory, exist_ok=True)

    if path.exists(location):
        os.popen(f"rm {location}")
    else:
        os.popen(f"touch {location}")


def append_tsv(issue, location):
    """
    appends rather than overwrites
    :return:
    """
    logging.info(">- WRITING TO OUTPUT TSV: %s", location)
    with open(location, "a+", newline="") as end_file:
        tsv_out = csv.writer(end_file, delimiter="\t")
        tsv_out.writerow(issue)


def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter


def main():
    """
    Main function to control essential aspects of script
    :return:
    """
    logging.config.dictConfig(json.loads(CONFIG))

    data_recorder = {}
    jira_jql = 'project IN ("ToL Assembly curation", "ToL Rapid Curation") AND status IN (Done, Submitted,"In Submission", "Post Processing++") ORDER BY key ASC'
    user, password, token = dotloader()

    args = parse_args()

    prep_folder(args.output)

    logging.info("Logging into Jira")
    jira = "https://jira.sanger.ac.uk"
    auth_jira = Jira(url=jira, username="ENV", password="ENV")

    logging.info("Sending JQL query")
    logging.debug("JQL = %s", jira_jql)
    issues = auth_jira.jql(
        jql=jira_jql,
        limit=args.hardlimit,
    )

    data_recorder["total tickets"] = issues["total"]
    limit_list = get_list_of_pages(args.hardlimit, issues["total"])
    logging.info("Calculating number of pages: %d", len(limit_list))

    total_list = []
    remov_list = []
    temp = [[250,300, 50]]
    for sublist in limit_list:
        logging.info("|>---- STARTING PAGE FOR ISSUES %s", sublist)
        page = get_pages(sublist[2], sublist, jira_jql, auth_jira)
        for i in page["issues"]:
            temp = i["key"]
            logging.info("|----> STARTING %s", temp)
            summary_search = re.search(r"(not being curated)", i["fields"]["summary"])
            if summary_search:
                if summary_search.group(1) == "(not being curated)":
                    remov_list.append(temp)
                    pass
            else:
                if i["fields"]["customfield_11608"] is None:
                    remov_list.append(temp)
                    pass

                jira_obj = JiraIssue(i)
                append_tsv(jira_obj.output_list(), args.output)
                total_list.append(i["key"])

    logging.info("JiraIssue Obj. list is: %s ", len(total_list))
    logging.info("No. of Tickets removed: %s ", len(remov_list))




if __name__ == "__main__":
    main()
