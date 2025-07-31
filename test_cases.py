## Test Case file
## Can be executed by running "pytest test_cases.py" in the command line

import pytest

# import functions for testing
from net_pay_calculator import main, input_employee_data, get_pay_rate, calculate_gross_pay, calculate_net_pay, connect_db





# Assigned to Fatimatou Ibrahim

from typing import Tuple
import pandas as pd

def input_employee_data(emp_list: pd.DataFrame) -> dict:
    """
    Prompts user for employee data and returns it as a dictionary.
    """
    # Validate Employee ID
    while True:
        try:
            e_id = int(input("Enter Employee ID: ").strip())
            if e_id not in emp_list.index:
                print(f"Employee ID {e_id} not found in database. Try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer for Employee ID.")

    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()

    while True:
        try:
            dependents = int(input("Enter Number of Dependents: "))
            if dependents < 0:
                print("Dependents cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for dependents.")

    while True:
        try:
            hours_worked = float(input("Enter Hours Worked: "))
            if hours_worked < 0:
                print("Hours worked cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for hours worked.")

    return {
        'employee_id': e_id,
        'first_name': first_name,
        'last_name': last_name,
        'dependents': dependents,
        'hours_worked': hours_worked
    }




# Assigned to Tyler Howard
def test_get_pay_rate() -> None:
    df = connect_db()
    assert get_pay_rate(1, df) == 20.00
    assert get_pay_rate(2, df) == 35.00
    assert get_pay_rate(4, df) == 17.77


# Assigned to DeMishia Jackson
def test_calculate_gross_pay() -> None:
    # (hours_worked, pay_rate)
    assert calculate_gross_pay(40, 20) == 800.00
    assert calculate_gross_pay(50, 35) == 1925.00
    assert calculate_gross_pay(40, 18.50) == 740.00
    assert calculate_gross_pay(45, 17.77) == 844.07


# Assigned to Willie Jones
def test_calculate_net_pay() -> None:
    assert calculate_net_pay(5000) == 4325
    assert calculate_net_pay(0) == 0
    assert calculate_net_pay(2300) == 1989.5


# Assigned to Kevin White
def test_record_results() -> None:
    pass
