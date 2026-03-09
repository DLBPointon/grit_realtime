# Implementing real time surveillance of genome curation impact on assembly quality
By Damon-Lee B Pointon (dp24)

This project was originally released as grit-realtime, in 2020-ish, as a RShiny app. 
However, due to organisational changes and issues with memory scaling in RShiny at the time
it was decided that this project should be re-written in the java framework javascript and HTML
as well as in a modernised tripartite docker container system controlled by docker-compose.

grt-v5 is the initial step towards creating a dashboard for GRIT (Genome Reference Informatics Team)
and offer decentralised access to metrics related to genome curation.

## Setup

Be aware that as of 09/03/2026, the python script takes ~8 miunutes to complete.

```
git clone https://github.com/DLBPointon/grit_realtime.git
cd grit_realtime

--> FILE_PATH is used by the docker_compose file to find the files needed
export FILE_PATH=$PWD

--> if using UV:
    uv venv
    source .venv/bin/activate
    uv pip install -r pyproject.toml
--> else use venv and pip
    python -m venv .venv
    source .venv/bin/activate
    pip install pyproject.toml

cp sample.env .env

--> NOTE: Add your JIRA_TOKEN to the env file or the script will fail

python scripts/jira_connect.py -e .env -s

docker compose up -d

--> Upon shutdown use the below to remove the existing database (doesn't delete the tsv file so you font need to run the jira_connect.py script again)

docker-compose down --volumes 
    
```

`-o` is the output path, by default this is `./grit-boot/output/jira_dump.tsv`
`-l` is the hardlimit, essentially a page limit of tickets.
`-e` is the path to the .env file
`-s` is silent, by default there is alot of logging


## Containers
<details>

grt-v5_server_1 : postgrest, a swagger api wrapper for PostgreSQL databases. It produces a usable API but with the one endpoint which is not ideal.

grt-v5_client_1 : The website it self, written via Bootstrap and HTML5.

grt-v5_db_1 : The PostgreSQL database, this will contain all of the information pulled from the attached scripts.

### Optional Container:

grt-v5_swagger_1 : A Swagger API UI.

</details>

## Scripts:
<details>

### Python:

jira_connect.py - Main script which pulls data from the Jira API, massages and outputs to a sorted TSV file ready for ingestion by the docker containers.

JiraIssue.py - An Class for the collection and parsing of individual tickets.

prefix_pull.py - An accessory script which pulls double letter assignments and clade information from the prefix_assignment_kj2.xlsx file.

prefix_assignments.py - Not technically a script but contains dictionaries on taxonomic information which is required by the main scripts.

### SQL:

10_db_init.sql - Creates the PSQL database table upon docker-compose up.

20_db_fill.sql - Fills the database table with information from jira_dump.tsv.sorted.

### R:

These are no longer in use but make up the old version of this projects graph generation and logic for reference.

grit_graphs.R - Graph generation script.

jira_data.R - Graph generation script.

### JavaScript

- index.html
  - maingraph{1/2}.js - Produces the 2 main graphs.
 
  - rightgraph{1/2}.js - 1 produces the box chart, 2 produces the pie chart or project numbers.
 

- datedash.html
  - date_graph.js - Produces a date time graph to be modified in the future to include pipeline versions,
    allows visualization of data over specific time frames.
    

- maingraphs.html
  - gevalgraph{1/2/3/4).js - These graphs mimic those found in the gEVAL paper [found here](https://www.biorxiv.org/content/10.1101/2020.08.12.247734v1.full).


- table.html
  - table_gen.js - Generates a table with select data as raw as possible for data verification.

</details>

## Proposal:
<details> 
Genome assembly curation has a significant impact on assembly quality,
and allows for the identification of opportunities for improvement within automated assembly generation.
Analysis of a multitude of assembly parameters is required, ideally in real time,
in order to document the impact and elucidate opportunities.
This is currently implemented by ad hoc extraction of the data from a Jira tracking database with a
perl script and subsequent graph generation in Excel,
a system that requires significant manual intervention. 

In order to streamline and further extend and adapt the process, I have produced
a system which uses Docker, Python (3.7) and Javascript to generate graphs in an
automated and consistent fashion.
Ultimately this results in the production of a dashboard/website that provides a real-time
report on curation impacts for specified data groups, within a specified time frame.

</details>

## Project Outline:
<details>

### Phase 1
#### Harvesting
Controlled by a python script, this will download all relevant
data from Jira as well as from family data from the ENA database.

In Python 3.7, this script accesses the Jira API and pulls data related to pre and post curation statistics as well as some taxonomic data.
It also performs some basic statistics just as percentage change in the pulled data.

This will only need to be used once in order to produce a "master" TSV file, used to later populate
the PostgreSQL database.

This utilises:

|Module | Reason | Implemented?|
|---|---|---|
|Argparse    | - for cli | [X] |
|csv         | - for tsv formatted writing| [X] |
|operator    | - used in sorting the tsv| [X] |
|regex (re)  | - for extensive regex use| [X] |
|maya        | - for string to datetime| [X] |
|datetime    | - for datetime to str conversion| [X] |
|jira        | - python-jira is a python api wrapper for Jira| [X] |
|logging     | - Used for logging information from script| [ ] |
| sys | - Used for safe exiting of the script | [X] |


### Phase 2
#### Docker-compose
In order to adopt a more modern approach, it was decided to utilise docker.
This would remove the need for front-end to be the point of reading data, calculation and presentation to graphs
this is now mostly moved to the PostgresSQL database and the API.
This allows the PSQL database to handle the data, the API to allow access for specific requested data and therefore
leaving only the graph production for the website.
Graphs are produced purely in Plotly.js which has proven to be a very flexible framework.

### Phase 3
#### Updating
This has been simplified and automated with a python3.7 script which uses the pre-existing database to
 return the most recent date in the database and use it as the minimum date in a query to Jira.
This will return a list of records (a python list of all required data).

</details>

## Usage

<details>

#### 1 - Git Clone

`git clone https://github.com/DLBPointon/grt-v5.git`
`cd grt-v5`

#### 2 - Download DB data
For testing there is a sample TSV in the output folder so this step can be skipped.

`python3 scripts/jira_connect.py {JIRA USER} {JIRA PASS} {SAVE}`

SAVE defaults to the output folder, as this is the folder to be used for docker later.
This is an option however in case colleagues want to run their own bespoke analysis on the data.

#### 3 - Docker-compose

At this point we can now compose the containers, much of this is automated via the docker-compose 
script as well as some sql scripts to initiate then fill the database. This can be started via the simple command:

`docker-compose up`

Spinning down the containers occurs with:
`docker-compose down --volumes`

#### 4 - Updating the db

Due to the requirement of this project to be pulling jira_db data in realtime
(realistically the db will only NEED to be updated once per day at the moment due to 
the number of tickets moving through the GRIT pipeline). 
I believe it is beneficial to have the updating script run as a crontab job.

`crontab -e`

```
* 8 * * * bash /home/grit/grt-v5/updater_cron.sh >> 
/home/grit/grt-v5/logs/`date +\%Y-\%m-\%d_\%H:\%M`.log 2>&1
```

This will directly update the psql database via calls to the JIRA_API and then the grt-API.
</details>

## TO-DO List
Found on the issues page
