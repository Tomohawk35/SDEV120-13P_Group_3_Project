import pytest
from net_pay_calculator import main, input_employee_data, get_pay_rate, calculate_gross_pay, calculate_taxes, record_results


def test_input_employee_data() -> None:
    pass


def test_get_pay_rate():
    assert get_pay_rate(1) == 20.00
    assert get_pay_rate(2) == 35.00
    assert get_pay_rate(4) == 17.77


def test_calculate_gross_pay() -> None:
    pass


def test_calculate_taxes() -> None:
    pass


def test_record_results() -> None:
    pass