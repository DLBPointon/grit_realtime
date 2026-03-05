from atlassian import Jira
import datetime


def get_status_change(auth, issue_obj):
    return auth.get_issue_status_changelog(issue_obj["key"])


def calculate_timedelta(start, end):
    datime_fmt = "%Y-%m-%dT%H:%M:%S.%f%z"
    return (
        datetime.datetime.strptime(end, datime_fmt)
        - datetime.datetime.strptime(start, datime_fmt)
    ).seconds


def calculate_time_in_status(creation_date, status_changelog):
    datime_fmt = "%Y-%m-%dT%H:%M:%S.%f%z"

    time_in_status = {}
    for i in status_changelog:
        if status_changelog.index(i) <= 0:
            time_in_status[i["from"]] = {
                "seconds": f"{calculate_timedelta(creation_date, i['date'])}s",
                "date_from": creation_date,
                "date_to": i["date"],
            }
        else:
            time_in_status[i["from"]] = {
                "seconds": f"{calculate_timedelta(status_changelog[status_changelog.index(i)-1]['date'], i['date'])}s",
                "date_from": status_changelog[status_changelog.index(i) - 1]["date"],
                "date_to": i["date"],
            }
    return time_in_status


def main():
    jira = "https://jira.sanger.ac.uk"
    auth_jira = Jira(url=jira, username="ENV", password="ENV")
    jira_jql = 'project IN ("ToL Assembly curation", "ToL Rapid Curation") AND status IN (Done, Submitted,"In Submission", "Post Processing++") ORDER BY key ASC'

    issues = auth_jira.jql(
        jql=jira_jql,
        limit=10,
    )

    for i in issues["issues"]:
        creation = i["fields"]["created"]
        changelog = get_status_change(auth_jira, i)
        time_in_status_dict = calculate_time_in_status(
            creation, changelog
        )  # <--- function for class
        print(time_in_status_dict)


if __name__ == "__main__":
    main()
