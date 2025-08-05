## Test Case file
## Can be executed by running "pytest test_cases.py" in the command line

import pytest
from unittest.mock import patch
import pandas as pd

# Import functions for testing
from net_pay_calculator import input_employee_data, calculate_gross_pay, calculate_net_pay, connect_db


# Sample employee "database" used across tests
emp_list = pd.DataFrame({
    'first_name': ['Fatimatou', 'Tyler'],
    'last_name': ['Ibrahim', 'Howard'],
    'dependents': [2, 3],
    'employee_rate': [20.00, 35.00]
}, index=[1, 2])


# Assigned to Fatimatou Ibrahim
def test_input_employee_data_valid():
    """Verify that input_employee_data returns correct data for a valid employee ID and matching details."""
    user_inputs = ['1', '40.00']  
    with patch('builtins.input', side_effect=user_inputs):
        result = input_employee_data(emp_list)
    assert result == {
        'employee_id': 1,
        'first_name': 'Fatimatou',
        'last_name': 'Ibrahim',
        'dependents': 2,
        'hours_worked': 40.00,
        'pay_rate': 20.00
    }


# Assigned to Fatimatou Ibrahim
def test_input_employee_data_invalid_then_valid_id():
    """
    Verify that input_employee_data rejects an invalid employee ID 
    and then proceeds correctly when a valid ID is entered.
    """
    user_inputs = ['999', '4', '45.00']
    with patch('builtins.input', side_effect=user_inputs):
        result = input_employee_data(emp_list)
    assert result == {
        'employee_id': 2,
        'first_name': 'Tyler',
        'last_name': 'Howard',
        'dependents': 3,
        'hours_worked': 45.00,
        'pay_rate': 17.77
    }


# Assigned to Tyler Howard
def test_get_pay_rate():
    """Ensure get_pay_rate returns the correct hourly rate for various employee IDs from the database."""
    df = connect_db()
    assert get_pay_rate(1, df) == 20.00
    assert get_pay_rate(4, df) == 17.77


# Assigned to DeMishia Jackson
def test_calculate_gross_pay():
    """
    Verify gross pay calculation under various conditions:
    - Only regular hours
    - Regular + Overtime hours
    - Different hourly rates
    """
    assert calculate_gross_pay(40, 20) == (40, 0, 800.00, 0.0, 800.00)
    assert calculate_gross_pay(50, 35) == (40, 10, 1400.00, 525.00, 1925.00)
    assert calculate_gross_pay(40, 18.50) == (40, 0, 740.00, 0.0, 740.00)
    assert calculate_gross_pay(45, 17.77) == (40, 5, 710.80, 133.27, 844.07)


# Assigned to Willie Jones
def test_calculate_net_pay():
    """
    Confirm net pay is correctly calculated after tax deductions:
    - High income
    - Zero income
    - Moderate income
    """
    assert calculate_net_pay(5000) == (280.00, 395.00, 4325.00)
    assert calculate_net_pay(0) == (0.00, 0.00, 0.00)
    assert calculate_net_pay(2300) == (128.80, 181.70, 1989.50)


# Assigned to Kevin White
def test_record_results():
    """Placeholder for record_results function – not yet implemented."""
    pass
