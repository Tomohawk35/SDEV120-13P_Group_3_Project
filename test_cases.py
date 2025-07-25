## Test Case file
## Can be executed by running "pytest test_cases.py" in the command line

import pytest

# import functions for testing
from net_pay_calculator import main, input_employee_data, get_pay_rate, calculate_gross_pay, calculate_taxes, record_results, connect_db




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
def test_calculate_taxes() -> None:
    pass

# # Test Case 1
# gross_pay = 5000
# state_tax, federal_tax, total_tax, net_pay = calculate_net_pay(gross_pay)
# assert round(net_pay, 2) == 4325, f"Test Case 1 Failed: Expected 4325, got {net_pay}"

# # Test Case 2
# gross_pay = 0
# state_tax, federal_tax, total_tax, net_pay = calculate_net_pay(gross_pay)
# assert round(net_pay, 2) == 0, f"Test Case 2 Failed: Expected 0, got {net_pay}"



# Assigned to Kevin White
def test_record_results() -> None:
    pass
