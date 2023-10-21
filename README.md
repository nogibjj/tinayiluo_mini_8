## Python Script interacting with SQL Database
[![CI](https://github.com/nogibjj/tinayiluo_sqlite_lab/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/tinayiluo_sqlite_lab/actions/workflows/cicd.yml)

Week 5 Mini Project

### Goal

+ Set up a CodeSpaces environment to automate the interaction between Python Script and SQL Database.

+ This environment should facilitate connection to an SQL database, execution of CRUD (Create, Read, Update, Delete) operations, and formulation of at least two distinct SQL queries.

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`) with Python Black, linting (`make lint`) with Ruff, and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

### Preperation

+ I forked the nogibjj/sqlite-lab.

+ I chose the Airline safety dataset `airline-safety.csv` from Github.

### Dataset Description

The dataset `airline-safety.csv` originates from the Aviation Safety Network and consolidates safety-related information for 56 airlines in a CSV file. It encompasses data on available seat kilometers flown every week and provides a detailed record of incidents, fatal accidents, and fatalities, each segregated into two time frames: 1985–1999 and 2000–2014.

#### [Resources](https://github.com/fivethirtyeight/data/tree/master/airline-safety) 

### Overview

This project creates a Python script that facilitate connection to an SQL database, execution of CRUD (Create, Read, Update, Delete) operations, and formulation of at least two distinct SQL queries. The specific steps involve: 

+ In my.lib, add extract.py, query.py and transform_load.py that perform:

* ETL-Query:  [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query

* [E] Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well.

* [T] Transform the data by cleaning, filtering, enriching, etc to get it ready for analysis.

* [L] Load the transformed data into a SQLite database table using Python's sqlite3 module.

* [Q] Write and execute at least 2 different SQL queries on the SQLite database to analyze and retrieve insights from the data.
      Perform CRUD (create, read, update, delete) operations

+ Convert the main.py into a command-line tool that run each step independantly

+ In test_main.py, test extract, transform, CRUD (Create, Read, Update, Delete), and general query

+ In make file, add extract, transform_load, and query command

+ Include an architectural diagram showing how the project works

### Description

Step 1: In my.lib: 

+ create extract.py

Defines a function called `extract` that can download a file from a given web address (url) and save it to a specified location (file_path) on my computer, creating the specified folder (directory) if it doesn’t already exist. By default, it is set to download an airline safety data file from GitHub and save it in a folder named “data”.

<img width="952" alt="Screen Shot 2023-10-01 at 12 24 57 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/f4de7967-2252-4b04-84ee-2365f7307eb7">

+ create transform_load.py

Defines a function called `load` that takes a CSV file containing airline safety data, reads it, and stores this data into a SQLite database. If the database table already exists, it removes it and creates a new one. After storing the data, it closes the database connection. The function is set by default to use a file named "airline-safety.csv" from the "data" folder.

<img width="737" alt="Screen Shot 2023-10-01 at 12 31 11 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/33bedbe6-7ec3-4218-9785-440084ebb933">

+ create quetry.py

This code provides a collection of functions to:

1. Insert new records into the "AirlineSafetyDB" database table.
2. Update existing records in that table.
3. Delete records from that table.
4. Read all records from that table.
5. Execute any general query on the database.

After performing any of the above operations, the code also logs the executed SQL queries into a markdown file, `query_log.md`, to keep a record of all database interactions.

<img width="829" alt="Screen Shot 2023-10-01 at 12 25 36 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/7e9e7bb2-c00d-43f1-96ec-b2911d78deab">

<img width="866" alt="Screen Shot 2023-10-01 at 12 25 55 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/8a8dbecf-bef2-4883-a54e-333b4bbd89a5">

<img width="766" alt="Screen Shot 2023-10-01 at 12 27 04 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/b28afc74-4f86-4a3a-81d2-4a87dc8b1fda">

<img width="701" alt="Screen Shot 2023-10-01 at 12 27 27 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/43a7e6da-ebe6-4713-8f95-7fe7b65c2331">

<img width="630" alt="Screen Shot 2023-10-01 at 12 30 08 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/ac474bbf-5a88-4b69-9c83-e857401be2ef">

Step 2: In `main.py`:

Provides a Command Line Interface (CLI) to perform various actions related to Extract, Transform, Load (ETL) and database operations, using functions from mylib.extract, mylib.transform_load, and mylib.query modules. 

1. I can run this script from the command line and choose an action like extract, transform_load, create_record, etc., along with the necessary arguments for each action.
2. The script parses my input and runs the corresponding function to perform the desired action, using functions imported from other modules.
3. For instance, if I want to update a record, I need to provide all the necessary information, and the script will call the update_record function with this information.
4. The results or any relevant messages are then printed out to the console.

<img width="921" alt="Screen Shot 2023-10-01 at 12 39 48 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/4d5e064f-5b91-4596-80e6-33044a021b0f">

<img width="840" alt="Screen Shot 2023-10-01 at 12 41 14 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/5f0ac261-58fa-4dab-98fe-c513d73bf313">

<img width="713" alt="Screen Shot 2023-10-01 at 12 41 41 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/f25d2854-ef98-4f8a-b4e8-ad704da42627">

Step 3: In `test_main.py`:
Runs different parts (actions) of the main.py script independently with specific inputs and checks whether they are working as expected, without any errors and, in some cases, with the expected output. If any of these tests fail, it means there might be a bug or an issue in the corresponding part of the main.py script.

<img width="669" alt="Screen Shot 2023-10-01 at 12 45 01 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/25a3ba9d-46d1-470b-8d48-ab404ddbb871">

<img width="778" alt="Screen Shot 2023-10-01 at 12 45 21 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/2eca90a1-c9fa-45c8-97ec-5b3c3c26daa1">

<img width="963" alt="Screen Shot 2023-10-01 at 12 45 45 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/71c4b428-46d4-445f-8c78-712e0468fb08">

<img width="642" alt="Screen Shot 2023-10-01 at 12 46 00 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/d55256a9-d05c-4452-9590-e173cdbcd311">

Step 4: In `Makefile`:

Add generate_and_push, extract, transform_load, query

<img width="1011" alt="Screen Shot 2023-10-01 at 12 47 56 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/b44e3fe5-b54a-4e8c-b8b7-652e6d76d930">

<img width="953" alt="Screen Shot 2023-10-01 at 12 48 13 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/c9b80c40-cca7-4b53-89db-cf0f6a5cdd3b">

Step 5: In Github Actions `cicd.yml`:
Add generate_and_push, extract, transform_load, query

<img width="939" alt="Screen Shot 2023-10-01 at 12 51 11 AM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/4076d058-f4e1-44a5-a11a-71e5e3a6c209">

step 6: [log of successful database operations](./query_log.md)

### Architectural Diagram

![SQLite Diagram drawio (1)](https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/6ddfa32e-d164-40fd-9413-8d0e1654bbc1)

### Make Format, Test, Lint, All Approval Image
<img width="851" alt="Screen Shot 2023-09-30 at 7 32 58 PM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/f0907017-4be5-49de-9e97-739047599c82">
<img width="1151" alt="Screen Shot 2023-09-30 at 7 36 13 PM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/3df48fef-a3a2-4f87-8c78-3517c6b4dbe3">
<img width="1136" alt="Screen Shot 2023-09-30 at 7 36 57 PM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/c6174dd0-4f34-47a4-b23e-815c4eab5be7">

