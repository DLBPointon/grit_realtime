import csv
import json
import re
import os
import sys
import time
from jira import JIRA
from requests_toolbelt import user_agent
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
V7   - Re-written to use the better JIRA library
     - Better Logging

"""

VERSION = "7.0.0"

def parse_args():
    parser = argparse.ArgumentParser(
        prog="GRIT-realtime",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(DESCRIPTION),
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Where to chuck the output?", default="./grit-boot/output/jira_dump.tsv"
    )
    parser.add_argument(
        "-l", "--hardlimit", type=int, help="Hardlimit for Jira. MAX is 1000.", default=800
    )
    parser.add_argument(
        "-e", "--env", help="Environ file", type=str, default=".env"
    )
    parser.add_argument(
        "-s", "--silent", help="Run without a rediculous amount of log", action='store_true'
    )

    parser.add_argument("-v", "--version", action="version", version=VERSION)

    return parser.parse_args()


def dotloader(env_arg: str) -> str | None:
    load_dotenv(env_arg)
    return os.getenv("JIRA_TOKEN") if os.getenv("JIRA_TOKEN") is not None else sys.exit(f"Where is the 'JIRA_TOKEN' its not in -e {env_arg}?")


def prep_folder(location: str) -> None:
    directory = "/".join(location.split("/")[:-1])
    os.makedirs(directory, exist_ok=True)

    if os.path.exists(location):
        os.popen(f"rm {location}")
    else:
        os.popen(f"touch {location}")


def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter


def quick_validate(output_file: str) -> int:
    with open("../grit-boot/output/jira_dump.tsv") as input:
        return len(input.readlines())


def main():
    """
    Main function to control essential aspects of script
    :return:
    """
    master_time = time.perf_counter()
    logging.config.dictConfig(json.loads(CONFIG))
    logging.info("Starting clock")

    jira_jql = 'project IN ("ToL Assembly curation", "ToL Rapid Curation") AND status IN (Done, Submitted,"In Submission", "Post Processing++") ORDER BY key ASC'

    args = parse_args()

    token = dotloader(args.env)

    logging.info("Cleaning old TSV")
    prep_folder(args.output)

    logging.info("Logging into Jira")
    auth_jira = JIRA(
        server = "https://jira.sanger.ac.uk",
        token_auth=(token),
        options={"headers": {"User-Agent": user_agent("GRIT_realtime", VERSION)}},
    )

    logging.info("Sending JQL query")
    logging.debug("JQL = %s", jira_jql)

    start_at = 0
    all_issues = []
    pages = 1
    remov_list = []
    total_list = 0

    # ---

    with open(args.output, "a+", newline="") as end_file:
        tsv_out = csv.writer(end_file, delimiter="\t")
        logging.info("|> WRITING TO OUTPUT TSV: %s", args.output)

        while True:

            logging.info("|--> STARTING PAGE %s FOR %s ISSUES", pages, args.hardlimit)
            pages += 1
            batch = auth_jira.search_issues(
                jira_jql,
                startAt=start_at,
                maxResults=args.hardlimit,
            )

            logging.info("|----> Issue Count so far is %s", len(all_issues))

            for i in batch:
                if not args.silent:
                    logging.info("|----> STARTING %s", i.key)
                assembly_stats = i.get_field("customfield_11608")
                summary_search = re.search(r"(not being curated)", i.fields.summary)
                if summary_search:
                    if summary_search.group(1) == "(not being curated)":
                        remov_list.append(i.key)
                        pass
                else:
                    if assembly_stats is None:
                        remov_list.append(i.key)
                        pass

                    jira_obj = JiraIssue(i)
                    total_list += 1

                    tsv_out.writerow(jira_obj.output_list())

                    # Rather than a TSV intermediary file, we could use pycopg2 for direct to DB inserts and the tsv be optionals
                    # https://www.geeksforgeeks.org/python/perform-insert-operations-with-psycopg2-in-python/
                    # Batch inset the valid chunks into the database

            all_issues.extend(batch)

            # ResultList has a .total with the server-side total
            if start_at + len(batch) >= batch.total:
                break

            start_at += len(batch)

            per_page = time.perf_counter()
            logging.info(f"|----> Time stamp at Page {pages} == {per_page - master_time:0.4f} Seconds")

    end_file.close

    file_lines = quick_validate(args.output)

    logging.info("| TOTAL NUMBER OF ISSUES | %s \t|", len(all_issues))
    logging.info("| No. of Tickets removed | %s \t|", len(remov_list))
    logging.info("| JiraIssue Obj. list is | %s \t|", total_list)
    logging.info("| Verified in out file   | %s \t|", file_lines)
    logging.info(f"| Tickets removed Inc --> {remov_list}")

    script_time = time.perf_counter()
    script_execution_time = script_time - master_time
    logging.info(f"| Time for script execution == {script_execution_time:0.4f} Seconds")


    if file_lines != total_list:
        logging.critical("Output file line count != valid jira tickets! Something's wrong outputting to file!")


if __name__ == "__main__":
    main()
