## Test Case file
## Can be executed by running "pytest test_cases.py" in the command line

import pytest

# import functions for testing
from net_pay_calculator import main, input_employee_data, get_pay_rate, calculate_gross_pay, calculate_taxes, record_results




# Assigned to Fatimatou Ibrahim
def test_input_employee_data_valid():
    result = input_employee_data("Fatima", "Ibrahim", 5, 2, 40.0)
    assert result == {
        "first_name": "Fatima",
        "last_name": "Ibrahim",
        "employee_id": 5,
        "dependents": 2,
        "hours_worked": 40.0
    }

def test_input_employee_data_invalid_id():
    with pytest.raises(ValueError) as e:
        input_employee_data("Test", "User", 9999, 1, 40.0)
    assert str(e.value) == "Employee ID 9999 not found in database."



# Assigned to Tyler Howard

def test_get_pay_rate() -> None:
    assert get_pay_rate(1) == 20.00
    assert get_pay_rate(2) == 35.00
    assert get_pay_rate(4) == 17.77


# Assigned to DeMishia jackson
def test_calculate_gross_pay() -> None:
    pass


# Assigned to Willie Jones
def test_calculate_taxes() -> None:
    pass


# Assigned to Kevin White
def test_record_results() -> None:
    pass