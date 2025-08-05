import pytest
import pandas as pd

from net_pay_calculator import calculate_gross_pay, calculate_net_pay, connect_db

# Sample employee "database" for isolated test, but tests mainly use the CSV via connect_db()

# Assigned to Fatimatou Ibrahim
def test_connect_db():
    df = connect_db()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert df.index.name == "employee_id"  # index must be employee_id

def test_db_has_required_fields():
    db = connect_db()
    required_fields = {'first_name', 'last_name', 'dependents', 'pay_rate'}
    assert required_fields.issubset(set(db.columns))
    assert db.index.name == 'employee_id'


# Assigned to Tyler Howard
def test_calculate_gross_pay():
    # calculate_gross_pay returns tuple (standard_hours, overtime_hours, standard_pay, overtime_pay, gross_pay)
    assert calculate_gross_pay(40, 20.0)[4] == 800.0
    assert calculate_gross_pay(45, 20.0)[4] == 950.0
    assert calculate_gross_pay(50, 35.0)[4] == 1925.0

# Assigned to DeMishia Jackson
def test_calculate_net_pay():
    # calculate_net_pay returns (state_tax_deduction, federal_tax_deduction, net_pay)
    state_tax, federal_tax, net = calculate_net_pay(5000)
    assert net == pytest.approx(5000 - state_tax - federal_tax)
    state_tax2, federal_tax2, net2 = calculate_net_pay(1000)
    assert net2 == pytest.approx(1000 - state_tax2 - federal_tax2)

# Assigned to Kevin White
def test_record_results():
    # Placeholder - no implementation needed now
    pass
