## Test Case file
## Can be executed by running "pytest test_cases.py" in the command line

import pytest
from unittest.mock import patch
import pandas as pd

# Import functions for testing
from net_pay_calculator import calculate_gross_pay, calculate_net_pay, connect_db

# Sample employee "database" used across tests
emp_list = pd.DataFrame({
    'first_name': ['Fatimatou', 'Tyler'],
    'last_name': ['Ibrahim', 'Howard'],
    'dependents': [2, 3],
    'pay_rate': [20.00, 35.00]
}, index=[1, 2])

# Assigned to Fatimatou Ibrahim
def test_connect_db():
    """Test if the employee database loads correctly."""
    df = connect_db()
    assert isinstance(df, list)
    assert len(df) > 0
    assert all("employee_id" in emp for emp in df)

# Assigned to Tyler Howard
def test_calculate_gross_pay():
    """Verify gross pay calculation for various hours."""
    assert calculate_gross_pay(40, 20.0) == 800.0
    assert calculate_gross_pay(45, 20.0) == 950.0
    assert calculate_gross_pay(50, 35.0) == 1925.0

# Assigned to DeMishia Jackson
def test_calculate_net_pay():
    """Check net pay calculations with and without dependents."""
    assert calculate_net_pay(5000, 0) == pytest.approx(4000.0)
    assert calculate_net_pay(5000, 2) == pytest.approx(4040.0)
    assert calculate_net_pay(1000, 3) == pytest.approx(840.0)

# Assigned to Kevin White
def test_data_integrity():
    """Ensure each employee has all required fields."""
    db = connect_db()
    for emp in db:
        assert set(emp.keys()) >= {'employee_id', 'first_name', 'last_name', 'dependents', 'pay_rate'}

# Assigned to Willie Jones
def test_record_results():
    """Placeholder for future test of result recording."""
    pass
