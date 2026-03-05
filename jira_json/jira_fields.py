jira_list = [
  {
    "id": "resolution",
    "name": "Resolution",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "resolution"
    ],
    "schema": {
      "type": "resolution",
      "system": "resolution"
    }
  },
  {
    "id": "customfield_10500",
    "name": "Approvers",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Approvers",
      "cf[10500]"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker",
      "customId": 10500
    }
  },
  {
    "id": "customfield_12800",
    "name": "Treeval data",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12800]",
      "Treeval data"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 12800
    }
  },
  {
    "id": "customfield_12802",
    "name": "Contamination",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12802]",
      "Contamination"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 12802
    }
  },
  {
    "id": "customfield_12801",
    "name": "Ploidy",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12801]",
      "Ploidy"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 12801
    }
  },
  {
    "id": "lastViewed",
    "name": "Last Viewed",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [
      "lastViewed"
    ],
    "schema": {
      "type": "datetime",
      "system": "lastViewed"
    }
  },
  {
    "id": "customfield_12000",
    "name": "B chromosomes",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "B chromosomes",
      "cf[12000]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 12000
    }
  },
  {
    "id": "customfield_13210",
    "name": "Chromosome list files",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[13210]",
      "Chromosome list files"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons",
      "customId": 13210
    }
  },
  {
    "id": "labels",
    "name": "Labels",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "labels"
    ],
    "schema": {
      "type": "array",
      "items": "string",
      "system": "labels"
    }
  },
  {
    "id": "customfield_10610",
    "name": "Source",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10610]",
      "Source"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10610
    }
  },
  {
    "id": "customfield_11700",
    "name": "Species list",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11700]",
      "Species list"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11700
    }
  },
  {
    "id": "customfield_10611",
    "name": "Investigation reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10611]",
      "Investigation reason"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10611
    }
  },
  {
    "id": "customfield_11702",
    "name": "Source",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11702]",
      "Source"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11702
    }
  },
  {
    "id": "customfield_10613",
    "name": "Workaround",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10613]",
      "Workaround"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10613
    }
  },
  {
    "id": "aggregatetimeoriginalestimate",
    "name": "Σ Original Estimate",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [],
    "schema": {
      "type": "number",
      "system": "aggregatetimeoriginalestimate"
    }
  },
  {
    "id": "customfield_10615",
    "name": "CAB",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "CAB",
      "cf[10615]"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker",
      "customId": 10615
    }
  },
  {
    "id": "issuelinks",
    "name": "Linked Issues",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [],
    "schema": {
      "type": "array",
      "items": "issuelinks",
      "system": "issuelinks"
    }
  },
  {
    "id": "assignee",
    "name": "Assignee",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "assignee"
    ],
    "schema": {
      "type": "user",
      "system": "assignee"
    }
  },
  {
    "id": "components",
    "name": "Component/s",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "component"
    ],
    "schema": {
      "type": "array",
      "items": "component",
      "system": "components"
    }
  },
  {
    "id": "customfield_10602",
    "name": "Change risk",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10602]",
      "Change risk"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10602
    }
  },
  {
    "id": "customfield_12900",
    "name": "WOSPI ToLID",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12900]",
      "WOSPI ToLID"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 12900
    }
  },
  {
    "id": "customfield_10607",
    "name": "Pending reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10607]",
      "Pending reason"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10607
    }
  },
  {
    "id": "customfield_10608",
    "name": "Product categorization",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10608]",
      "Product categorization"
    ],
    "schema": {
      "type": "option-with-child",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselect",
      "customId": 10608
    }
  },
  {
    "id": "customfield_10609",
    "name": "Operational categorization",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10609]",
      "Operational categorization"
    ],
    "schema": {
      "type": "option-with-child",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselect",
      "customId": 10609
    }
  },
  {
    "id": "subtasks",
    "name": "Sub-Tasks",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [
      "subtasks"
    ],
    "schema": {
      "type": "array",
      "items": "issuelinks",
      "system": "subtasks"
    }
  },
  {
    "id": "reporter",
    "name": "Reporter",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "reporter"
    ],
    "schema": {
      "type": "user",
      "system": "reporter"
    }
  },
  {
    "id": "customfield_11800",
    "name": "Systems and Software",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11800]",
      "Systems and Software"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiselect",
      "customId": 11800
    }
  },
  {
    "id": "customfield_11803",
    "name": "Value",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11803]",
      "Value"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 11803
    }
  },
  {
    "id": "customfield_11802",
    "name": "Acceptance Criteria",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Acceptance Criteria",
      "cf[11802]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11802
    }
  },
  {
    "id": "customfield_11805",
    "name": "Version",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11805]",
      "Version"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11805
    }
  },
  {
    "id": "customfield_11806",
    "name": "URL",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11806]",
      "URL"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:url",
      "customId": 11806
    }
  },
  {
    "id": "progress",
    "name": "Progress",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [
      "progress"
    ],
    "schema": {
      "type": "progress",
      "system": "progress"
    }
  },
  {
    "id": "votes",
    "name": "Votes",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [
      "votes"
    ],
    "schema": {
      "type": "votes",
      "system": "votes"
    }
  },
  {
    "id": "worklog",
    "name": "Log Work",
    "custom": False,
    "orderable": True,
    "navigable": False,
    "searchable": True,
    "clauseNames": [],
    "schema": {
      "type": "array",
      "items": "worklog",
      "system": "worklog"
    }
  },
  {
    "id": "archivedby",
    "name": "Archiver",
    "custom": False,
    "orderable": True,
    "navigable": False,
    "searchable": True,
    "clauseNames": [],
    "schema": {
      "type": "user",
      "system": "archivedby"
    }
  },
  {
    "id": "issuetype",
    "name": "Issue Type",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "issuetype",
      "type"
    ],
    "schema": {
      "type": "issuetype",
      "system": "issuetype"
    }
  },
  {
    "id": "project",
    "name": "Project",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "project"
    ],
    "schema": {
      "type": "project",
      "system": "project"
    }
  },
  {
    "id": "customfield_12326",
    "name": "Budget Code",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Budget Code",
      "cf[12326]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 12326
    }
  },
  {
    "id": "resolutiondate",
    "name": "Resolved",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "resolutiondate",
      "resolved"
    ],
    "schema": {
      "type": "datetime",
      "system": "resolutiondate"
    }
  },
  {
    "id": "watches",
    "name": "Watchers",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [
      "watchers"
    ],
    "schema": {
      "type": "watches",
      "system": "watches"
    }
  },
  {
    "id": "customfield_12321",
    "name": "TiCom Representative",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12321]",
      "TiCom Representative"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 12321
    }
  },
  {
    "id": "customfield_12200",
    "name": "Treeval",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12200]",
      "Treeval"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 12200
    }
  },
  {
    "id": "customfield_12320",
    "name": "Have existing platforms been considered?",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12320]",
      "Have existing platforms been considered?"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons",
      "customId": 12320
    }
  },
  {
    "id": "customfield_12323",
    "name": "Cloud Provider",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12323]",
      "Cloud Provider"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons",
      "customId": 12323
    }
  },
  {
    "id": "customfield_12322",
    "name": "Label Project or Account with UBW Budget Code",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12322]",
      "Label Project or Account with UBW Budget Code"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 12322
    }
  },
  {
    "id": "customfield_12325",
    "name": "Technical Contact has a Sanger Account",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12325]",
      "Technical Contact has a Sanger Account"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons",
      "customId": 12325
    }
  },
  {
    "id": "customfield_12324",
    "name": "Technical Contact",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12324]",
      "Technical Contact"
    ],
    "schema": {
      "type": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:userpicker",
      "customId": 12324
    }
  },
  {
    "id": "customfield_12316",
    "name": "Admin Access to Cloud Project/Account",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Admin Access to Cloud Project/Account",
      "cf[12316]"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker",
      "customId": 12316
    }
  },
  {
    "id": "customfield_11105",
    "name": "Change start date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11105]",
      "Change start date"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:datetime",
      "customId": 11105
    }
  },
  {
    "id": "customfield_11106",
    "name": "Change completion date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11106]",
      "Change completion date"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:datetime",
      "customId": 11106
    }
  },
  {
    "id": "customfield_12315",
    "name": "Sanger Email",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12315]",
      "Sanger Email"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 12315
    }
  },
  {
    "id": "customfield_10810",
    "name": "Customer",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10810]",
      "Customer"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10810
    }
  },
  {
    "id": "customfield_11900",
    "name": "Team TOL",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11900]",
      "Team TOL"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11900
    }
  },
  {
    "id": "customfield_12318",
    "name": "Cloud Project/Account Name",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12318]",
      "Cloud Project/Account Name"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 12318
    }
  },
  {
    "id": "customfield_11107",
    "name": "Urgency",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11107]",
      "Urgency"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11107
    }
  },
  {
    "id": "customfield_10811",
    "name": "People",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10811]",
      "People"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker",
      "customId": 10811
    }
  },
  {
    "id": "customfield_11108",
    "name": "Change managers",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11108]",
      "Change managers"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker",
      "customId": 11108
    }
  },
  {
    "id": "customfield_11109",
    "name": "Reviewer",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11109]",
      "Reviewer"
    ],
    "schema": {
      "type": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:userpicker",
      "customId": 11109
    }
  },
  {
    "id": "customfield_12319",
    "name": "Technical Non-Sanger Contact Reason ",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12319]",
      "Technical Non-Sanger Contact Reason "
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 12319
    }
  },
  {
    "id": "customfield_13408",
    "name": "YAML",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[13408]",
      "YAML"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 13408
    }
  },
  {
    "id": "customfield_10814",
    "name": "Success Criteria",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10814]",
      "Success Criteria"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10814
    }
  },
  {
    "id": "customfield_10815",
    "name": "Output",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10815]",
      "Output"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 10815
    }
  },
  {
    "id": "customfield_10816",
    "name": "Objectives",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10816]",
      "Objectives"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10816
    }
  },
  {
    "id": "customfield_10818",
    "name": "issueFunction",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10818]",
      "issueFunction"
    ],
    "schema": {
      "type": "any",
      "custom": "com.onresolve.jira.groovy.groovyrunner:jqlFunctionsCustomFieldType",
      "customId": 10818
    }
  },
  {
    "id": "updated",
    "name": "Updated",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "updated",
      "updatedDate"
    ],
    "schema": {
      "type": "datetime",
      "system": "updated"
    }
  },
  {
    "id": "timeoriginalestimate",
    "name": "Original Estimate",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [
      "originalEstimate",
      "timeoriginalestimate"
    ],
    "schema": {
      "type": "number",
      "system": "timeoriginalestimate"
    }
  },
  {
    "id": "description",
    "name": "Description",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "description"
    ],
    "schema": {
      "type": "string",
      "system": "description"
    }
  },
  {
    "id": "customfield_12310",
    "name": "Data Management Plan",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12310]",
      "Data Management Plan"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons",
      "customId": 12310
    }
  },
  {
    "id": "customfield_12312",
    "name": "Principal Investigator",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12312]",
      "Principal Investigator"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 12312
    }
  },
  {
    "id": "customfield_11102",
    "name": "Impact",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11102]",
      "Impact"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11102
    }
  },
  {
    "id": "customfield_12311",
    "name": "Keep Infrastructure Up to Date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12311]",
      "Keep Infrastructure Up to Date"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 12311
    }
  },
  {
    "id": "customfield_11103",
    "name": "Change type",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11103]",
      "Change type"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11103
    }
  },
  {
    "id": "customfield_12314",
    "name": "Data Owner",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12314]",
      "Data Owner"
    ],
    "schema": {
      "type": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:userpicker",
      "customId": 12314
    }
  },
  {
    "id": "timetracking",
    "name": "Time Tracking",
    "custom": False,
    "orderable": True,
    "navigable": False,
    "searchable": True,
    "clauseNames": [],
    "schema": {
      "type": "timetracking",
      "system": "timetracking"
    }
  },
  {
    "id": "customfield_11104",
    "name": "Change reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11104]",
      "Change reason"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11104
    }
  },
  {
    "id": "customfield_12313",
    "name": "Ensure principle of least privileged is applied",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12313]",
      "Ensure principle of least privileged is applied"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 12313
    }
  },
  {
    "id": "customfield_12305",
    "name": "RnD Team",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12305]",
      "RnD Team"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 12305
    }
  },
  {
    "id": "customfield_12304",
    "name": "Strategy",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12304]",
      "Strategy"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 12304
    }
  },
  {
    "id": "customfield_12307",
    "name": "No internet by Default",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12307]",
      "No internet by Default"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 12307
    }
  },
  {
    "id": "customfield_12306",
    "name": "Number of replicates",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12306]",
      "Number of replicates"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 12306
    }
  },
  {
    "id": "customfield_10801",
    "name": "Start Date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10801]",
      "Start Date"
    ],
    "schema": {
      "type": "date",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:datepicker",
      "customId": 10801
    }
  },
  {
    "id": "customfield_12309",
    "name": "Cloud environment use",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12309]",
      "Cloud environment use"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 12309
    }
  },
  {
    "id": "customfield_12308",
    "name": "Data Management Plan Details",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12308]",
      "Data Management Plan Details"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 12308
    }
  },
  {
    "id": "customfield_10806",
    "name": "Samples",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10806]",
      "Samples"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10806
    }
  },
  {
    "id": "customfield_10807",
    "name": "Duration",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10807]",
      "Duration"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 10807
    }
  },
  {
    "id": "customfield_10809",
    "name": "RCP Number",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10809]",
      "RCP Number"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 10809
    }
  },
  {
    "id": "summary",
    "name": "Summary",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "summary"
    ],
    "schema": {
      "type": "string",
      "system": "summary"
    }
  },
  {
    "id": "customfield_11691",
    "name": "Quota",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11691]",
      "Quota"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11691
    }
  },
  {
    "id": "customfield_11694",
    "name": "Deployment",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11694]",
      "Deployment"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11694
    }
  },
  {
    "id": "customfield_10000",
    "name": "Development",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10000]",
      "Development"
    ],
    "schema": {
      "type": "any",
      "custom": "com.atlassian.jira.plugins.jira-development-integration-plugin:devsummary",
      "customId": 10000
    }
  },
  {
    "id": "customfield_12301",
    "name": "TOR Link",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12301]",
      "TOR Link"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 12301
    }
  },
  {
    "id": "customfield_11696",
    "name": "Users added",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11696]",
      "Users added"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11696
    }
  },
  {
    "id": "customfield_12300",
    "name": "Custom Description",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12300]",
      "Custom Description"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 12300
    }
  },
  {
    "id": "customfield_12303",
    "name": "Sample List",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12303]",
      "Sample List"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 12303
    }
  },
  {
    "id": "customfield_12302",
    "name": "Benchling link",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Benchling link",
      "cf[12302]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 12302
    }
  },
  {
    "id": "customfield_11697",
    "name": "Users removed",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11697]",
      "Users removed"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11697
    }
  },
  {
    "id": "environment",
    "name": "Environment",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "environment"
    ],
    "schema": {
      "type": "string",
      "system": "environment"
    }
  },
  {
    "id": "duedate",
    "name": "Due Date",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "due",
      "duedate"
    ],
    "schema": {
      "type": "date",
      "system": "duedate"
    }
  },
  {
    "id": "comment",
    "name": "Comment",
    "custom": False,
    "orderable": True,
    "navigable": False,
    "searchable": True,
    "clauseNames": [
      "comment"
    ],
    "schema": {
      "type": "comments-page",
      "system": "comment"
    }
  },
  {
    "id": "customfield_11681",
    "name": "Manual joins",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11681]",
      "Manual joins"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 11681
    }
  },
  {
    "id": "customfield_11680",
    "name": "Workaround",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11680]",
      "Workaround"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11680
    }
  },
  {
    "id": "customfield_11683",
    "name": "Contamination Level Summary",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11683]",
      "Contamination Level Summary"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11683
    }
  },
  {
    "id": "customfield_11682",
    "name": "Change risk",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11682]",
      "Change risk"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11682
    }
  },
  {
    "id": "customfield_10110",
    "name": "Epic Link",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10110]",
      "Epic Link"
    ],
    "schema": {
      "type": "any",
      "custom": "com.pyxis.greenhopper.jira:gh-epic-link",
      "customId": 10110
    }
  },
  {
    "id": "fixVersions",
    "name": "Fix Version/s",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "fixVersion"
    ],
    "schema": {
      "type": "array",
      "items": "version",
      "system": "fixVersions"
    }
  },
  {
    "id": "customfield_11685",
    "name": "HiC Juicer file",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11685]",
      "HiC Juicer file"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11685
    }
  },
  {
    "id": "customfield_10111",
    "name": "Story Points",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10111]",
      "Story Points"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 10111
    }
  },
  {
    "id": "customfield_11684",
    "name": "BigWig Coverage file URL",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "BigWig Coverage file URL",
      "cf[11684]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:url",
      "customId": 11684
    }
  },
  {
    "id": "customfield_11687",
    "name": "Access required",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Access required",
      "cf[11687]"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11687
    }
  },
  {
    "id": "customfield_10104",
    "name": "Epic Name",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10104]",
      "Epic Name"
    ],
    "schema": {
      "type": "string",
      "custom": "com.pyxis.greenhopper.jira:gh-epic-label",
      "customId": 10104
    }
  },
  {
    "id": "customfield_11678",
    "name": "Important",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11678]",
      "Important"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11678
    }
  },
  {
    "id": "customfield_11677",
    "name": "Contamination files",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11677]",
      "Contamination files"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11677
    }
  },
  {
    "id": "customfield_10105",
    "name": "Epic Status",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10105]",
      "Epic Status"
    ],
    "schema": {
      "type": "option",
      "custom": "com.pyxis.greenhopper.jira:gh-epic-status",
      "customId": 10105
    }
  },
  {
    "id": "customfield_10106",
    "name": "Epic Colour",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10106]",
      "Epic Colour"
    ],
    "schema": {
      "type": "string",
      "custom": "com.pyxis.greenhopper.jira:gh-epic-color",
      "customId": 10106
    }
  },
  {
    "id": "customfield_11679",
    "name": "Purged Primary Fasta File",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11679]",
      "Purged Primary Fasta File"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11679
    }
  },
  {
    "id": "customfield_10107",
    "name": "Team",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10107]",
      "Team"
    ],
    "schema": {
      "type": "any",
      "custom": "com.atlassian.teams:rm-teams-custom-field-team",
      "customId": 10107
    }
  },
  {
    "id": "customfield_10108",
    "name": "Rank",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10108]",
      "Rank"
    ],
    "schema": {
      "type": "any",
      "custom": "com.pyxis.greenhopper.jira:gh-lexo-rank",
      "customId": 10108
    }
  },
  {
    "id": "customfield_10109",
    "name": "Sprint",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10109]",
      "Sprint"
    ],
    "schema": {
      "type": "array",
      "items": "string",
      "custom": "com.pyxis.greenhopper.jira:gh-sprint",
      "customId": 10109
    }
  },
  {
    "id": "customfield_11670",
    "name": "Change start date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11670]",
      "Change start date"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:datetime",
      "customId": 11670
    }
  },
  {
    "id": "customfield_11672",
    "name": "trio_hyb assembly information",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11672]",
      "trio_hyb assembly information"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11672
    }
  },
  {
    "id": "customfield_11671",
    "name": "Data copied",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11671]",
      "Data copied"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11671
    }
  },
  {
    "id": "customfield_10100",
    "name": "Parent Link",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10100]",
      "Parent Link"
    ],
    "schema": {
      "type": "any",
      "custom": "com.atlassian.jpo:jpo-custom-field-parent",
      "customId": 10100
    }
  },
  {
    "id": "customfield_11674",
    "name": "Submission note",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11674]",
      "Submission note"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11674
    }
  },
  {
    "id": "priority",
    "name": "Priority",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "priority"
    ],
    "schema": {
      "type": "priority",
      "system": "priority"
    }
  },
  {
    "id": "customfield_10101",
    "name": "Target start",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10101]",
      "Target start"
    ],
    "schema": {
      "type": "date",
      "custom": "com.atlassian.jpo:jpo-custom-field-baseline-start",
      "customId": 10101
    }
  },
  {
    "id": "customfield_11673",
    "name": "gEVAL QC/Audit Checks",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11673]",
      "gEVAL QC/Audit Checks"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11673
    }
  },
  {
    "id": "customfield_11676",
    "name": "Species Name",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11676]",
      "Species Name"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11676
    }
  },
  {
    "id": "customfield_10102",
    "name": "Target end",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10102]",
      "Target end"
    ],
    "schema": {
      "type": "date",
      "custom": "com.atlassian.jpo:jpo-custom-field-baseline-end",
      "customId": 10102
    }
  },
  {
    "id": "customfield_10103",
    "name": "Original story points",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10103]",
      "Original story points"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jpo:jpo-custom-field-original-story-points",
      "customId": 10103
    }
  },
  {
    "id": "customfield_11675",
    "name": "hyb_assembly file",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11675]",
      "hyb_assembly file"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11675
    }
  },
  {
    "id": "customfield_11667",
    "name": "Curator QC",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11667]",
      "Curator QC"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11667
    }
  },
  {
    "id": "customfield_11666",
    "name": "Submission files",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11666]",
      "Submission files"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11666
    }
  },
  {
    "id": "customfield_11669",
    "name": "Orientation",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11669]",
      "Orientation"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11669
    }
  },
  {
    "id": "customfield_11668",
    "name": "Assembled by",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Assembled by",
      "cf[11668]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11668
    }
  },
  {
    "id": "timeestimate",
    "name": "Remaining Estimate",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [
      "remainingEstimate",
      "timeestimate"
    ],
    "schema": {
      "type": "number",
      "system": "timeestimate"
    }
  },
  {
    "id": "versions",
    "name": "Affects Version/s",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "affectedVersion"
    ],
    "schema": {
      "type": "array",
      "items": "version",
      "system": "versions"
    }
  },
  {
    "id": "status",
    "name": "Status",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "status"
    ],
    "schema": {
      "type": "status",
      "system": "status"
    }
  },
  {
    "id": "issuekey",
    "name": "Key",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [
      "id",
      "issue",
      "issuekey",
      "key"
    ]
  },
  {
    "id": "customfield_11661",
    "name": "TPF URL",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11661]",
      "TPF URL"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:url",
      "customId": 11661
    }
  },
  {
    "id": "customfield_11660",
    "name": "Datatype Available",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11660]",
      "Datatype Available"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11660
    }
  },
  {
    "id": "customfield_11663",
    "name": "Paternal contamination file",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11663]",
      "Paternal contamination file"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11663
    }
  },
  {
    "id": "customfield_11665",
    "name": "Investigation reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11665]",
      "Investigation reason"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11665
    }
  },
  {
    "id": "archiveddate",
    "name": "Archived",
    "custom": False,
    "orderable": True,
    "navigable": False,
    "searchable": True,
    "clauseNames": [],
    "schema": {
      "type": "datetime",
      "system": "archiveddate"
    }
  },
  {
    "id": "customfield_11664",
    "name": "Haplotype",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11664]",
      "Haplotype"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11664
    }
  },
  {
    "id": "customfield_11656",
    "name": "Released to",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11656]",
      "Released to"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11656
    }
  },
  {
    "id": "customfield_11655",
    "name": "Change type",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11655]",
      "Change type"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11655
    }
  },
  {
    "id": "customfield_11658",
    "name": "Metadata files",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11658]",
      "Metadata files"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11658
    }
  },
  {
    "id": "customfield_11657",
    "name": "Curator",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11657]",
      "Curator"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11657
    }
  },
  {
    "id": "aggregatetimeestimate",
    "name": "Σ Remaining Estimate",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [],
    "schema": {
      "type": "number",
      "system": "aggregatetimeestimate"
    }
  },
  {
    "id": "customfield_11659",
    "name": "Curated autosomes",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11659]",
      "Curated autosomes"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 11659
    }
  },
  {
    "id": "creator",
    "name": "Creator",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "creator"
    ],
    "schema": {
      "type": "user",
      "system": "creator"
    }
  },
  {
    "id": "customfield_11650",
    "name": "Telomere motif",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11650]",
      "Telomere motif"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11650
    }
  },
  {
    "id": "aggregateprogress",
    "name": "Σ Progress",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [],
    "schema": {
      "type": "progress",
      "system": "aggregateprogress"
    }
  },
  {
    "id": "customfield_11531",
    "name": "External issue ID",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11531]",
      "External issue ID"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11531
    }
  },
  {
    "id": "customfield_11652",
    "name": "Impact",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11652]",
      "Impact"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11652
    }
  },
  {
    "id": "customfield_10200",
    "name": "Flagged",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10200]",
      "Flagged"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 10200
    }
  },
  {
    "id": "customfield_11651",
    "name": "Telomere motif k-mer length",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11651]",
      "Telomere motif k-mer length"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 11651
    }
  },
  {
    "id": "customfield_11654",
    "name": "Pending reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11654]",
      "Pending reason"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11654
    }
  },
  {
    "id": "customfield_11645",
    "name": "Chromosome result",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11645]",
      "Chromosome result"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11645
    }
  },
  {
    "id": "customfield_11403",
    "name": "Specimen ID",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11403]",
      "Specimen ID"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11403
    }
  },
  {
    "id": "customfield_11644",
    "name": "Change managers",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11644]",
      "Change managers"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker",
      "customId": 11644
    }
  },
  {
    "id": "customfield_11402",
    "name": "New species name",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11402]",
      "New species name"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11402
    }
  },
  {
    "id": "customfield_11647",
    "name": "Change completion date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11647]",
      "Change completion date"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:datetime",
      "customId": 11647
    }
  },
  {
    "id": "customfield_11404",
    "name": "New ToLID",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11404]",
      "New ToLID"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11404
    }
  },
  {
    "id": "customfield_11646",
    "name": "gEVAL Analyses Completed",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11646]",
      "gEVAL Analyses Completed"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11646
    }
  },
  {
    "id": "customfield_11649",
    "name": "Release to:",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11649]",
      "Release to:"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11649
    }
  },
  {
    "id": "customfield_11648",
    "name": "Gfastats",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11648]",
      "Gfastats"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11648
    }
  },
  {
    "id": "timespent",
    "name": "Time Spent",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [
      "timespent"
    ],
    "schema": {
      "type": "number",
      "system": "timespent"
    }
  },
  {
    "id": "aggregatetimespent",
    "name": "Σ Time Spent",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": [],
    "schema": {
      "type": "number",
      "system": "aggregatetimespent"
    }
  },
  {
    "id": "customfield_11641",
    "name": "Expected sex",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11641]",
      "Expected sex"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11641
    }
  },
  {
    "id": "customfield_11640",
    "name": "Decontaminated fasta",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11640]",
      "Decontaminated fasta"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11640
    }
  },
  {
    "id": "customfield_11401",
    "name": "Current ToLID",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11401]",
      "Current ToLID"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11401
    }
  },
  {
    "id": "customfield_11643",
    "name": "HiGlass entry",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11643]",
      "HiGlass entry"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11643
    }
  },
  {
    "id": "customfield_11642",
    "name": "Bionano index file location",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Bionano index file location",
      "cf[11642]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11642
    }
  },
  {
    "id": "customfield_11400",
    "name": "Current species name",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11400]",
      "Current species name"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11400
    }
  },
  {
    "id": "customfield_10423",
    "name": "Document Link",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10423]",
      "Document Link"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 10423
    }
  },
  {
    "id": "customfield_10302",
    "name": "Organizations",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10302]",
      "Organizations"
    ],
    "schema": {
      "type": "array",
      "items": "sd-customerorganization",
      "custom": "com.atlassian.servicedesk:sd-customer-organizations",
      "customId": 10302
    }
  },
  {
    "id": "customfield_11633",
    "name": "CAB",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "CAB",
      "cf[11633]"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker",
      "customId": 11633
    }
  },
  {
    "id": "customfield_10424",
    "name": "Change start date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10424]",
      "Change start date"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:datetime",
      "customId": 10424
    }
  },
  {
    "id": "customfield_10303",
    "name": "Satisfaction",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10303]",
      "Satisfaction"
    ],
    "schema": {
      "type": "any",
      "custom": "com.atlassian.servicedesk:sd-request-feedback",
      "customId": 10303
    }
  },
  {
    "id": "customfield_11636",
    "name": "Assemblies assessment",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Assemblies assessment",
      "cf[11636]"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11636
    }
  },
  {
    "id": "customfield_10425",
    "name": "Change completion date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10425]",
      "Change completion date"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:datetime",
      "customId": 10425
    }
  },
  {
    "id": "customfield_10304",
    "name": "Satisfaction date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10304]",
      "Satisfaction date"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.servicedesk:sd-request-feedback-date",
      "customId": 10304
    }
  },
  {
    "id": "customfield_10305",
    "name": "Linked major incidents",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10305]",
      "Linked major incidents"
    ],
    "schema": {
      "type": "any",
      "custom": "com.atlassian.servicedesk.incident-management-plugin:sd-incidents-link",
      "customId": 10305
    }
  },
  {
    "id": "customfield_10426",
    "name": "Time to resolution",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10426]",
      "Time to resolution"
    ],
    "schema": {
      "type": "sd-servicelevelagreement",
      "custom": "com.atlassian.servicedesk:sd-sla-field",
      "customId": 10426
    }
  },
  {
    "id": "customfield_11635",
    "name": "Urgency",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11635]",
      "Urgency"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11635
    }
  },
  {
    "id": "customfield_10306",
    "name": "Approvals",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Approvals",
      "cf[10306]"
    ],
    "schema": {
      "type": "sd-approvals",
      "custom": "com.atlassian.servicedesk.approvals-plugin:sd-approvals",
      "customId": 10306
    }
  },
  {
    "id": "customfield_11638",
    "name": "Haplotype",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11638]",
      "Haplotype"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons",
      "customId": 11638
    }
  },
  {
    "id": "customfield_10427",
    "name": "Time to approve normal change",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10427]",
      "Time to approve normal change"
    ],
    "schema": {
      "type": "sd-servicelevelagreement",
      "custom": "com.atlassian.servicedesk:sd-sla-field",
      "customId": 10427
    }
  },
  {
    "id": "customfield_11637",
    "name": "Change reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11637]",
      "Change reason"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11637
    }
  },
  {
    "id": "customfield_10428",
    "name": "Time to first response",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10428]",
      "Time to first response"
    ],
    "schema": {
      "type": "sd-servicelevelagreement",
      "custom": "com.atlassian.servicedesk:sd-sla-field",
      "customId": 10428
    }
  },
  {
    "id": "customfield_10429",
    "name": "Time to close after resolution",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10429]",
      "Time to close after resolution"
    ],
    "schema": {
      "type": "sd-servicelevelagreement",
      "custom": "com.atlassian.servicedesk:sd-sla-field",
      "customId": 10429
    }
  },
  {
    "id": "customfield_11639",
    "name": "Yaml attached?",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11639]",
      "Yaml attached?"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11639
    }
  },
  {
    "id": "workratio",
    "name": "Work Ratio",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "workratio"
    ],
    "schema": {
      "type": "number",
      "system": "workratio"
    }
  },
  {
    "id": "thumbnail",
    "name": "Images",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": False,
    "clauseNames": []
  },
  {
    "id": "created",
    "name": "Created",
    "custom": False,
    "orderable": False,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "created",
      "createdDate"
    ],
    "schema": {
      "type": "datetime",
      "system": "created"
    }
  },
  {
    "id": "customfield_11630",
    "name": "Resolution Reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11630]",
      "Resolution Reason"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11630
    }
  },
  {
    "id": "customfield_10420",
    "name": "Backout/Rollback Plan",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Backout/Rollback Plan",
      "cf[10420]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10420
    }
  },
  {
    "id": "customfield_10421",
    "name": "Investigation reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10421]",
      "Investigation reason"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10421
    }
  },
  {
    "id": "customfield_11632",
    "name": "Manual haplotig removals",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11632]",
      "Manual haplotig removals"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 11632
    }
  },
  {
    "id": "customfield_10300",
    "name": "Request participants",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10300]",
      "Request participants"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.servicedesk:sd-request-participants",
      "customId": 10300
    }
  },
  {
    "id": "customfield_11631",
    "name": "Accession Data",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Accession Data",
      "cf[11631]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11631
    }
  },
  {
    "id": "customfield_10422",
    "name": "Cherwell #",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10422]",
      "Cherwell #"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 10422
    }
  },
  {
    "id": "customfield_10301",
    "name": "Customer Request Type",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10301]",
      "Customer Request Type"
    ],
    "schema": {
      "type": "sd-customerrequesttype",
      "custom": "com.atlassian.servicedesk:vp-origin",
      "customId": 10301
    }
  },
  {
    "id": "customfield_10412",
    "name": "Communication Plan",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10412]",
      "Communication Plan"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10412
    }
  },
  {
    "id": "customfield_11623",
    "name": "Product categorization",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11623]",
      "Product categorization"
    ],
    "schema": {
      "type": "option-with-child",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselect",
      "customId": 11623
    }
  },
  {
    "id": "customfield_10413",
    "name": "Change reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10413]",
      "Change reason"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10413
    }
  },
  {
    "id": "customfield_11622",
    "name": "Synteny source",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11622]",
      "Synteny source"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11622
    }
  },
  {
    "id": "customfield_11625",
    "name": "Assembly Version",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Assembly Version",
      "cf[11625]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11625
    }
  },
  {
    "id": "customfield_10414",
    "name": "Reason for Change",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10414]",
      "Reason for Change"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10414
    }
  },
  {
    "id": "customfield_11624",
    "name": "Assembly type",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Assembly type",
      "cf[11624]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11624
    }
  },
  {
    "id": "customfield_10415",
    "name": "Workaround",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10415]",
      "Workaround"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10415
    }
  },
  {
    "id": "customfield_10416",
    "name": "Change risk",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10416]",
      "Change risk"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10416
    }
  },
  {
    "id": "customfield_11627",
    "name": "Sample ID",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11627]",
      "Sample ID"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11627
    }
  },
  {
    "id": "customfield_10417",
    "name": "Existing Process",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10417]",
      "Existing Process"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10417
    }
  },
  {
    "id": "customfield_11626",
    "name": "Maternal contamination file",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11626]",
      "Maternal contamination file"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11626
    }
  },
  {
    "id": "customfield_11629",
    "name": "HiC kit",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11629]",
      "HiC kit"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11629
    }
  },
  {
    "id": "customfield_10418",
    "name": "Source",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10418]",
      "Source"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10418
    }
  },
  {
    "id": "customfield_10419",
    "name": "Change managers",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10419]",
      "Change managers"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker",
      "customId": 10419
    }
  },
  {
    "id": "customfield_11628",
    "name": "Submission date",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11628]",
      "Submission date"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:datetime",
      "customId": 11628
    }
  },
  {
    "id": "customfield_13001",
    "name": "Taxon ID",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[13001]",
      "Taxon ID"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 13001
    }
  },
  {
    "id": "customfield_10410",
    "name": "Audit Status",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Audit Status",
      "cf[10410]"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10410
    }
  },
  {
    "id": "customfield_11621",
    "name": "Purged Haplotig Fasta File",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11621]",
      "Purged Haplotig Fasta File"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11621
    }
  },
  {
    "id": "customfield_11620",
    "name": "External Contact",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11620]",
      "External Contact"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11620
    }
  },
  {
    "id": "customfield_10411",
    "name": "Urgency",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10411]",
      "Urgency"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10411
    }
  },
  {
    "id": "customfield_12701",
    "name": "Outcome",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[12701]",
      "Outcome"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 12701
    }
  },
  {
    "id": "customfield_10401",
    "name": "Product categorization",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10401]",
      "Product categorization"
    ],
    "schema": {
      "type": "option-with-child",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselect",
      "customId": 10401
    }
  },
  {
    "id": "customfield_11612",
    "name": "trio_hyb location",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11612]",
      "trio_hyb location"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11612
    }
  },
  {
    "id": "customfield_11611",
    "name": "Assessment summary",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Assessment summary",
      "cf[11611]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11611
    }
  },
  {
    "id": "customfield_10402",
    "name": "Impact",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10402]",
      "Impact"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10402
    }
  },
  {
    "id": "customfield_11614",
    "name": "Genome note",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11614]",
      "Genome note"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11614
    }
  },
  {
    "id": "customfield_10403",
    "name": "Scheduled Completion Time",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10403]",
      "Scheduled Completion Time"
    ],
    "schema": {
      "type": "date",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:datepicker",
      "customId": 10403
    }
  },
  {
    "id": "security",
    "name": "Security Level",
    "custom": False,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "level"
    ],
    "schema": {
      "type": "securitylevel",
      "system": "security"
    }
  },
  {
    "id": "customfield_10404",
    "name": "Operational categorization",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10404]",
      "Operational categorization"
    ],
    "schema": {
      "type": "option-with-child",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselect",
      "customId": 10404
    }
  },
  {
    "id": "customfield_11613",
    "name": "Resolution summary",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11613]",
      "Resolution summary"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11613
    }
  },
  {
    "id": "attachment",
    "name": "Attachment",
    "custom": False,
    "orderable": True,
    "navigable": False,
    "searchable": True,
    "clauseNames": [
      "attachments"
    ],
    "schema": {
      "type": "array",
      "items": "attachment",
      "system": "attachment"
    }
  },
  {
    "id": "customfield_10405",
    "name": "Affected Services",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Affected Services",
      "cf[10405]"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10405
    }
  },
  {
    "id": "customfield_11616",
    "name": "gEVAL Data/Setup",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11616]",
      "gEVAL Data/Setup"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11616
    }
  },
  {
    "id": "customfield_11615",
    "name": "Manual breaks",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11615]",
      "Manual breaks"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 11615
    }
  },
  {
    "id": "customfield_10406",
    "name": "Pending reason",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10406]",
      "Pending reason"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10406
    }
  },
  {
    "id": "customfield_10407",
    "name": "Change type",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10407]",
      "Change type"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 10407
    }
  },
  {
    "id": "customfield_11618",
    "name": "gEVAL QC/Audit Completion",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11618]",
      "gEVAL QC/Audit Completion"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11618
    }
  },
  {
    "id": "customfield_10408",
    "name": "CAB",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "CAB",
      "cf[10408]"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker",
      "customId": 10408
    }
  },
  {
    "id": "customfield_11617",
    "name": "Curated allosomes",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11617]",
      "Curated allosomes"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11617
    }
  },
  {
    "id": "customfield_10409",
    "name": "Root cause",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[10409]",
      "Root cause"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 10409
    }
  },
  {
    "id": "customfield_11619",
    "name": "HiC checklist",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11619]",
      "HiC checklist"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11619
    }
  },
  {
    "id": "customfield_13111",
    "name": "Hap2 Gfastats",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[13111]",
      "Hap2 Gfastats"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 13111
    }
  },
  {
    "id": "customfield_13110",
    "name": "Hap2 Assembly Statistics",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[13110]",
      "Hap2 Assembly Statistics"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 13110
    }
  },
  {
    "id": "customfield_11610",
    "name": "Manual inversions",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11610]",
      "Manual inversions"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 11610
    }
  },
  {
    "id": "customfield_11601",
    "name": "Observed sex",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11601]",
      "Observed sex"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select",
      "customId": 11601
    }
  },
  {
    "id": "customfield_11603",
    "name": "Pretext file Location",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11603]",
      "Pretext file Location"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11603
    }
  },
  {
    "id": "customfield_11602",
    "name": "Curation Files",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11602]",
      "Curation Files"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 11602
    }
  },
  {
    "id": "customfield_13109",
    "name": "Hap2 Chromosome Result",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[13109]",
      "Hap2 Chromosome Result"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 13109
    }
  },
  {
    "id": "customfield_11605",
    "name": "Expected Karyotype",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11605]",
      "Expected Karyotype"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 11605
    }
  },
  {
    "id": "customfield_11604",
    "name": "Operational categorization",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11604]",
      "Operational categorization"
    ],
    "schema": {
      "type": "option-with-child",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselect",
      "customId": 11604
    }
  },
  {
    "id": "customfield_11607",
    "name": "Chromsome Naming",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11607]",
      "Chromsome Naming"
    ],
    "schema": {
      "type": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons",
      "customId": 11607
    }
  },
  {
    "id": "customfield_11606",
    "name": "Purged artifact fasta file",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11606]",
      "Purged artifact fasta file"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
      "customId": 11606
    }
  },
  {
    "id": "customfield_11609",
    "name": "Release Version",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "cf[11609]",
      "Release Version"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 11609
    }
  },
  {
    "id": "customfield_11608",
    "name": "Assembly statistics",
    "custom": True,
    "orderable": True,
    "navigable": True,
    "searchable": True,
    "clauseNames": [
      "Assembly statistics",
      "cf[11608]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
      "customId": 11608
    }
  }
]