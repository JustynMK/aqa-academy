# aqa-academy

# Coding rules
## Excluded folders
1. .venv folder: 
This folder is excluded. For information on creating a virtual environment using venv, refer to the official Python documentation: https://docs.python.org/3/library/venv.html
2. Reports: 
Exclude this folder to avoid conflicts during Git pushes.

## Dependency updates
1. Major library versions should be reviewed once per month.

## How to:

1. Setting Up Your Environment:

    1.1 Create a virtual environment in the .venv folder.

    1.2 Install dependencies from the requirements.txt file.

2. Before Committing: 

    2.1 Run the Black code formatter. 

    2.2 Check your code with Flake8 -> run flake8 tool.

    2.3 Organize imports using isort -> run isort tool.

3. Running Tests:

    3.1. Execute pytest command: `pytest . -s -v` staying from the root of the framework.

    3.2 Generate a report with pytest: `pytest . -s -v --html=reports/report.html —self-contained-html`

## Structure of the framework
1. tests - folder for test files.
2. reports - folder to storage local reports
3. src/applications - folder contains system-under-test abstractions.
4. src/config - folder for configuration settings for the framework.
5. src/helpers - folder for single-use functions and utilities.
