## Test Case file
## Can be executed by running "pytest test_cases.py" in the command line

import pytest

# import functions for testing
from net_pay_calculator import main, input_employee_data, get_pay_rate, calculate_gross_pay, calculate_net_pay, connect_db

# Assigned to Fatimatou Ibrahim
import pytest
from unittest.mock import patch
import pandas as pd
from net_pay_calculator import input_employee_data

# Simulate an employee "database"
emp_list = pd.DataFrame({
    'first_name': ['Fatima', 'Tyler'],
    'last_name': ['Ibrahim', 'Howard'],
    'dependents': [2, 3]
}, index=[1, 4])  

def test_input_employee_data_valid():
    user_inputs = ['1', 'Fatima', 'Ibrahim', '2', '20.00']
    with patch('builtins.input', side_effect=user_inputs):
        result = input_employee_data(emp_list)
    assert result == {
        'employee_id': 1,
        'first_name': 'Fatima',
        'last_name': 'Ibrahim',
        'dependents': 2,
        'hours_worked': 20.00
    }

def test_input_employee_data_invalid_then_valid_id():
    user_inputs = ['999', '4', 'Tyler', 'Howard', '3', '17.77']
    with patch('builtins.input', side_effect=user_inputs):
        result = input_employee_data(emp_list)
    assert result == {
        'employee_id': 4,
        'first_name': 'Tyler',
        'last_name': 'Howard',
        'dependents': 3,
        'hours_worked': 17.77
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
