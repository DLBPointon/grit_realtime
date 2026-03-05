from jira_fields import jira_list
import json

jira_dict = {}

for i in jira_list:
    print(i["id"])
    jira_dict[i["id"]] = {"normal_name": i["name"], "is_custom?": i["custom"]}


with open("my.json", "w") as f:
    json.dump(jira_dict, f)
