# SDEV120-13P_Group_3_Project
Group 3 Project for SDEV120 at IvyTech

## Project Overview

This project is intended to meet the following requirements:
- Take inputs from the user, including employee_id, first name, last name, number of dependents, and hours worked
- Query an existing database with the entered employee_id for the associated pay rate
- Calculate standard pay, overtime pay, gross pay, state and federal taxes, and net pay
- Output all data to a data file
- Continue taking input until user exits


# Command Guide

## Create and activate virtual environment
python -m venv venv
source venv/bin/activate     # On Mac/Linux
### or
venv\Scripts\activate        # On Windows

## Install dependencies
pip install -r requirements.txt

## Run tests
pytest test_cases.py

## Freeze environment (if needed)
pip freeze > requirements.txt

## Deactivate environment (when done)
deactivate