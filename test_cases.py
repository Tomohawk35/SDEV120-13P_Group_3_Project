## Test Case file
## Can be executed by running "pytest test_cases.py" in the command line

import pytest

# import functions for testing
from net_pay_calculator import main, input_employee_data, get_pay_rate, calculate_gross_pay, calculate_net_pay, record_results, connect_db, check_employee_id




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
