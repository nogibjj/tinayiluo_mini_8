## Rewrite a Python Script in Rust
[![Python CI/CD Pipeline](https://github.com/nogibjj/tinayiluo_mini_8/actions/workflows/pythonCI.yml/badge.svg)](https://github.com/nogibjj/tinayiluo_mini_8/actions/workflows/pythonCI.yml)

[![Rust CI/CD Pipeline](https://github.com/nogibjj/tinayiluo_mini_8/actions/workflows/rustCI.yml/badge.svg)](https://github.com/nogibjj/tinayiluo_mini_8/actions/workflows/rustCI.yml)

Mini project 8: Rewrite a Python Script in Rust

### Architectural Diagram

![SQLite Diagram drawio (1)](https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/6ddfa32e-d164-40fd-9413-8d0e1654bbc1)

### Goal

This project delivers a comprehensive Data Extraction, Transformation, Loading (ETL) tool, alongside Querying (CRUD) capabilities, developed using Python and Rust each. The process entails taking an existing Python script for ETL-Query and rewrite it in rust using Github Copilot. The project highlights improvements in speed and resource usage after switching Python to Rust. 

This toolkit offers a suite of functions for ETL operations on datasets, facilitating queries on a SQLite database. It comprehensively covers CRUD (Create, Read, Update, Delete) operations, logging all queries to two Markdown file, `python_query_log.md` and `rust_query_log.md`, to aid in the tracking and analysis of executed commands and comparing the speed and resource usage for Python and Rust on the `Extract` operation. 

The operational workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`) with Python Black, linting (`make lint`) with Ruff, and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

### Preperation

+ I used the nogibjj/tinayiluo_sqlite_lab template.

+ I chose the Airline safety dataset `airline-safety.csv` from Github.

### Dataset Background

The dataset `airline-safety.csv` originates from the Aviation Safety Network and consolidates safety-related information for 56 airlines in a CSV file. It encompasses data on available seat kilometers flown every week and provides a detailed record of incidents, fatal accidents, and fatalities, each segregated into two time frames: 1985–1999 and 2000–2014.

#### [Resources](https://github.com/fivethirtyeight/data/tree/master/airline-safety) 

### Description on Python Workflow

Step 1: In `my.lib`: 

+ create `extract.py`

Defines a function called `extract` that can download a file from a given web address (url) and save it to a specified location (file_path) on my computer, creating the specified folder (directory) if it doesn’t already exist. By default, it is set to download an airline safety data file from GitHub and save it in a folder named “data”.

+ create `transform_load.py`

Defines a function called `load` that takes a CSV file containing airline safety data, reads it, and stores this data into a SQLite database. If the database table already exists, it removes it and creates a new one. After storing the data, it closes the database connection. The function is set by default to use a file named "airline-safety.csv" from the "data" folder.

+ create `query.py`

This code provides a collection of functions to:

- Insert new records into the "AirlineSafetyDB" database table.

- Update existing records in that table.

- Delete records from that table.

- Read all records from that table.

- Execute any general query on the database.

After performing any of the above operations, the code also logs the executed SQL queries into a markdown file, query_log.md, to keep a record of all database interactions.

Step 2: In `main.py`:

Provides a Command Line Interface (CLI) to perform various actions related to Extract, Transform, Load (ETL) and database operations, using functions from mylib.extract, mylib.transform_load, and mylib.query modules.

- It measures the initial time and memory usage of the process.

- Based on the action passed in via the command line, it routes the call to the appropriate function and performs the necessary action. For example: If the action is "extract", it extracts data and then logs the time taken and memory used.

- After executing the action, it captures the elapsed time and memory difference, printing it and logging it.

Step 3: In `test_main.py`:

Runs different parts (actions) of the main.py script independently with specific inputs and checks whether they are working as expected. test general query

Step 4: In `Makefile`:

Defines a series of tasks related to Python development, ranging from installing dependencies to running tests and linting the codebase.

```
python_extract:
	python main.py extract

python_transform_load:
	python main.py transform_load

python_create:
	python main.py general_query "INSERT INTO AirlineSafetyDB (airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, fatalities_85_99, incidents_00_14, fatal_accidents_00_14, fatalities_00_14) VALUES ('Happy Airlines', 965346770, 1, 1, 1, 1, 1, 1);"

python_read:
	python main.py general_query "SELECT * FROM AirlineSafetyDB WHERE airline = 'Happy Airlines';"

python_update:
	python main.py general_query "UPDATE AirlineSafetyDB SET airline='Happy Airlines', avail_seat_km_per_week=965346770, incidents_85_99=0, fatal_accidents_85_99=0, fatalities_85_99=0, incidents_00_14=0, fatal_accidents_00_14=0, fatalities_00_14=0 WHERE id=57;"

python_delete:
	python main.py general_query "DELETE FROM AirlineSafetyDB WHERE id=57;"
```

Step 5: In Github Actions `pythonCI.yml`:

This workflow primarily revolves around checking out the project's code, installing dependencies, linting, formatting, testing a Python application. It executes the make python_extract command to perform data extraction, which is later used for comparison in speed and resource usage with Rust.

step 6: [log of successful python database operations](./python_query_log.md)

### Description on Rust Workflow

Step 1: Rust Initiation using `cargo init`

initialize a new Rust project by running ‘cargo init` inside the directory, it will set up a new Rust project by:

* Creating a Cargo.toml file, which contains configuration data, dependencies, and other metadata about the Rust project.

* Creating a src directory with a main.rs file for binary projects or lib.rs for libraries.

* Generating a .gitignore file if the directory is not inside an existing git repository. 

Step 2: Rust Dependencies Installation

In Cargo.toml specify metadatas and dependencies

* Project Metadata: It provides metadata about the Rust package, such as its name, version, authors, and edition.

```
[package]
name = "tina_yi_sqlite"
version = "0.1.0"
edition = "2021"
```
* Dependencies: It lists external packages (also known as "crates") that the project depends on. This allows Cargo to automatically fetch and build these dependencies when compiling the project.

```
[dependencies]
reqwest = { version = "^0.11", features = ["blocking"] }
rusqlite = "^0.29"
csv = "^1.0"
assert_cmd = "^2.0"
predicates = "0.9"
sys-info = "0.7.0"
```
The Following Steps Are Performed Using `Github Copilot` Translation From Python to Rust

Step 3: src `lib.rs`: 

The `lib.rs` file provides a set of functions that work in tandem to extract data from a URL, store it as a local CSV file, load this data into a SQLite database, and provide querying capabilities, with all executed queries being logged for future reference.

Step 4: src `main.rs`:

The `main.rs` file provides a command-line interface (CLI) for users to execute three main actions (ETL-Query) related to a dataset: extracting it from a URL, transforming and loading it into a SQLite database , and executing SQL queries against the database.

- It measures the initial time and memory usage of the process.

- Based on the action passed in via the command line, it routes the call to the appropriate function and performs the necessary action. For example: If the action is "extract", it extracts data and then logs the time taken and memory used.

- After executing the action, it captures the elapsed time and memory difference, printing it and logging it.

Step 5: tests `etl.test.rs`:

The `etl_tests.rs` file provides unit tests for the core ETL functions of the tina_yi_sqlite crate, helping ensure the integrity and correctness of the crate's functionality.

Step 6: `Makefile`:

The Makefile provides a set of tasks to automate various aspects of developing, testing, and managing a Rust project.

```
extract:
	cargo run extract

transform_load:
	cargo run transform_load

create:
	cargo run query "INSERT INTO AirlineSafetyDB (airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, fatalities_85_99, incidents_00_14, fatal_accidents_00_14, fatalities_00_14) VALUES ('Happy Airlines', 965346770, 1, 1, 1, 1, 1, 1);"

read:
	cargo run query "SELECT * FROM AirlineSafetyDB WHERE airline = 'Happy Airlines';"

update:
	cargo run query "UPDATE AirlineSafetyDB SET airline='Happy Airlines', avail_seat_km_per_week=965346770, incidents_85_99=0, fatal_accidents_85_99=0, fatalities_85_99=0, incidents_00_14=0, fatal_accidents_00_14=0, fatalities_00_14=0 WHERE id=57;"

delete:
	cargo run query "DELETE FROM AirlineSafetyDB WHERE id=57;"
```

Step 7: Github Actions `rustCI.yml`:

The CI/CD pipeline provides a comprehensive process for building, formatting, linting and testing the Rust project on GitHub. It executes the make extract command to perform data extraction, which is later used for comparison in speed and resource usage with Python.

Step 6: [log of successful rust database operations](./rust_query_log.md)

### Result

[Performance Comparison Report](./Performance_Comparison_Report_Rust_VS_Python.md) 

[The Python Time and Memory Usage File](./python_query_log.md)

[The Rust Time and Memory Usage File](./rust_query_log.md)

In a performance comparison of the extract action on a SQL Database using Python and Rust, Rust demonstrated notably enhanced efficiency in both runtime and memory usage. While Python's execution times ranged from 351.13 ms to 551.25 ms and consumed memory between 3,840.0 kB to 4,096.0 kB, Rust completed the task in just 197.75 ms and used 0 kB of memory. This stark disparity can be attributed to Rust's efficient memory management, its compilation to machine code, and potential differences in library implementations. While Python offers flexibility and ease of use, Rust's efficiency, predictable performance, and optimal resource management make it an excellent choice for tasks where performance is a key criterion.

<img width="1065" alt="Screen Shot 2023-10-21 at 11 54 47 PM" src="https://github.com/nogibjj/tinayiluo_mini_8/assets/143360909/bb602a5e-612e-4f7e-8daa-a7ac4c6e077b">

<img width="1077" alt="Screen Shot 2023-10-21 at 11 56 50 PM" src="https://github.com/nogibjj/tinayiluo_mini_8/assets/143360909/01509506-f50c-418b-9c27-af159a35f7e2">

### Make Format, Test, Lint, All Approval Image for Python 
* Format code make python_format
* Lint code make python_lint
* Test code make python_test

<img width="1026" alt="Screen Shot 2023-10-22 at 10 07 21 PM" src="https://github.com/nogibjj/tinayiluo_mini_8/assets/143360909/72b7bb89-16f8-498f-a32b-2c10048ae537">

<img width="1027" alt="Screen Shot 2023-10-22 at 10 07 39 PM" src="https://github.com/nogibjj/tinayiluo_mini_8/assets/143360909/0789d121-30c3-4d34-b429-e54da75ca0db">

### Make Format, Test, Lint, All Approval Image for Rust 
* Format code make format
* Lint code make lint
* Test code make test

<img width="1010" alt="Screen Shot 2023-10-22 at 10 08 49 PM" src="https://github.com/nogibjj/tinayiluo_mini_8/assets/143360909/6a4d74f5-84c1-4eba-a71a-dc5b893d5bd0">

<img width="1016" alt="Screen Shot 2023-10-22 at 10 09 20 PM" src="https://github.com/nogibjj/tinayiluo_mini_8/assets/143360909/10fd7022-f967-490e-9f22-7b747b5ebb21">
