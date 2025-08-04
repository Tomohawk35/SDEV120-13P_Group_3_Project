## Code is intended to calculate net pay for any number of employees and record it in a spreadsheet

import pandas as pd
from typing import Tuple

# Database where employee info and pay rates are stored
RATE_TABLE = "employee_rates.csv"  # CSV includes: employee_id, first_name, last_name, dependents, employee_rate

# Tax rates
STATE_TAX = 0.056
FEDERAL_TAX = 0.079

# Sentinel value (not currently used but reserved for future)
SENTINEL = "000"

# While loop control
enter_data = True


# Main function is assigned to Ashley Kemp // Completed by Tyler Howard and Fatimatou Ibrahim
def main():
    # Connect and load employee info + rates from one CSV
    rate_table = connect_db()

    global enter_data

    while enter_data:
        pay_stub_data = []

        # Get employee data from user input and rate table
        employee_data = input_employee_data(rate_table)

        # Extract info for calculations
        employee_id = employee_data['employee_id']
        first_name = employee_data['first_name']
        last_name = employee_data['last_name']
        dependents = employee_data['dependents']
        hours_worked = employee_data['hours_worked']
        pay_rate = employee_data['pay_rate']

        # Store data in list for saving later
        pay_stub_data.extend([
            employee_id, first_name, last_name, dependents, hours_worked, pay_rate
        ])

        # Calculate gross pay details
        standard_hours, overtime_hours, standard_pay, overtime_pay, gross_pay = calculate_gross_pay(hours_worked, pay_rate)
        pay_stub_data.extend([standard_hours, overtime_hours, standard_pay, overtime_pay, gross_pay])

        # Calculate net pay and deductions
        state_tax_ded, fed_tax_ded, net_pay = calculate_net_pay(gross_pay)
        pay_stub_data.extend([state_tax_ded, fed_tax_ded, net_pay])

        # Save results to file
        record_results(pay_stub_data)

        # Ask user if want to continue entering data
        value = do_continue()
        while value not in ("y", "n"):
            value = do_continue()

        if value == "n":
            enter_data = False

    print("Program complete.")


# Assigned to Fatimatou Ibrahim
def input_employee_data(rate_table: pd.DataFrame) -> dict:
    while True:
        try:
            employee_id = int(input("Enter Employee ID: ").strip())
            if employee_id in rate_table.index:
                break
            else:
                print("Employee ID not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get employee info from the rate table directly
    employee_info = rate_table.loc[employee_id]
    first_name = employee_info['first_name']
    last_name = employee_info['last_name']
    dependents = employee_info['dependents']
    pay_rate = float(employee_info['employee_rate'])  # Make sure your CSV header is 'employee_rate'

    while True:
        try:
            hours_worked = float(input("Enter Hours Worked: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a number for hours worked.")

    return {
        'employee_id': employee_id,
        'first_name': first_name,
        'last_name': last_name,
        'dependents': dependents,
        'hours_worked': hours_worked,
        'pay_rate': pay_rate
    }


# Assigned to Tyler Howard
def connect_db() -> pd.DataFrame:
    try:
        # Read employee_rates.csv with employee_id as index
        rate_data: pd.DataFrame = pd.read_csv(RATE_TABLE, header=0, index_col=0)
        return rate_data
    except Exception as e:
        print(f"Unable to read from {RATE_TABLE}: {e}")
        exit(1)  # Stop program if file not found


# Assigned to DeMishia Jackson
def calculate_gross_pay(hours_worked: float, pay_rate: float) -> Tuple[float, float, float, float, float]:
    standard_hours: float = min(hours_worked, 40)
    overtime_hours: float = max(hours_worked - 40, 0)
    standard_pay: float = round(standard_hours * pay_rate, 2)
    overtime_pay: float = round(overtime_hours * pay_rate * 1.5, 2)
    gross_pay: float = standard_pay + overtime_pay
    return standard_hours, overtime_hours, standard_pay, overtime_pay, gross_pay


# Assigned to Willie Jones
def calculate_net_pay(gross_pay: float) -> Tuple[float, float, float]:
    state_tax_deduction = round(STATE_TAX * gross_pay, 2)
    federal_tax_deduction = round(FEDERAL_TAX * gross_pay, 2)
    net_pay = round(gross_pay - state_tax_deduction - federal_tax_deduction, 2)
    return state_tax_deduction, federal_tax_deduction, net_pay


# Assigned to Kevin White // Completed by Tyler Howard
def record_results(data: list) -> None:
    column_headers = [
        "EmployeeID", "FirstName", "LastName", "NumDependents", "HoursWorked", "PayRate",
        "StandardHours", "OvertimeHours", "StandardPay", "OvertimePay", "GrossPay",
        "StateTax", "FedTax", "NetPay"
    ]
    results_table = pd.DataFrame([data], columns=column_headers)
    # Append results without header and index
    results_table.to_csv("results.csv", mode="a", index=False, header=False)


def do_continue() -> str:
    return input("Would you like to input more data? (y/n): ")


if __name__ == "__main__":
    main()
