## Code is intended to calculate net pay for any number of employees and record it in a spreadsheet

# used to manage the database file for pulling pay rates
# more information can be found at https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv
import pandas as pd 
from typing import Tuple


# database where employee pay rates are stored
RATE_TABLE: str = "employee_rates.csv"


# tax rates
STATE_TAX: float = 0.056
FEDERAL_TAX: float = 0.079

# sentinel value
SENTINEL: str = "000"

# while loop control
enter_data: bool = True


# Main function is assigned to Ashley Kemp
def main():
    rate_table = connect_db()
    emp_list = pd.read_csv('employee_data.csv', index_col='employee_id')

    global enter_data

    while enter_data:
        pay_stub_data = []

        employee_data = input_employee_data(emp_list)

        employee_id = employee_data['employee_id']
        first_name = employee_data['first_name']
        last_name = employee_data['last_name']
        dependents = employee_data['dependents']
        hours_worked = employee_data['hours_worked']

        pay_stub_data.append(employee_id)
        pay_stub_data.append(first_name)
        pay_stub_data.append(last_name)
        pay_stub_data.append(dependents)
        pay_stub_data.append(hours_worked)

        pay_rate = get_pay_rate(employee_id, rate_table)
        pay_stub_data.append(pay_rate)

        standard_hours, overtime_hours, standard_pay, overtime_pay, gross_pay = calculate_gross_pay(hours_worked, pay_rate)
        pay_stub_data.extend([standard_hours, overtime_hours, standard_pay, overtime_pay, gross_pay])

        state_tax_ded, fed_tax_ded, net_pay = calculate_net_pay(gross_pay)
        pay_stub_data.extend([state_tax_ded, fed_tax_ded, net_pay])

        record_results(pay_stub_data)

        value = do_continue()
        while value not in ("y", "n"):
            value = do_continue()

        if value == "n":
            enter_data = False

    print("Program complete.")



def do_continue():
    return input("Would you like to input more data? (y/n): ")

# Assigned to Fatimatou Ibrahim

def input_employee_data(emp_list: pd.DataFrame) -> dict:
    while True:
        try:
            employee_id = int(input("Enter Employee ID: ").strip())
            if employee_id in emp_list.index:
                break
            else:
                print("Employee ID not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()

    while True:
        try:
            dependents = int(input("Enter Number of Dependents: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a number for dependents.")

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
        'hours_worked': hours_worked
    }



# Assigned to Tyler Howard
# The hourly rate should be pulled from a database using the employee ID as the primary key.
def connect_db() -> pd.DataFrame: 
    # read the csv file and store a dataframe ("table")
    try:
        rate_data: pd.DataFrame = pd.read_csv(RATE_TABLE, header=0, index_col=0) 
        return rate_data
    except:
        print(f"Unable to read from {RATE_TABLE}")


# extracts the rate from the dataframe based on the input employee id
def get_pay_rate(emp_id: int, emp_rates: pd.DataFrame) -> float: 
    return emp_rates['employee_rate'].loc[emp_id]


# Assigned to DeMishia jackson
def calculate_gross_pay(hours_worked: float, pay_rate: float) -> Tuple[float, float, float, float, float]:
    standard_hours: float = min(hours_worked, 40)
    overtime_hours: float = max(hours_worked - 40, 0)
    standard_pay: float = round(standard_hours * pay_rate, 2)
    overtime_pay: float = round(overtime_hours * pay_rate * 1.5, 2)
    gross_pay: float = round(standard_pay + overtime_pay, 2)
    return standard_hours, overtime_hours, standard_pay, overtime_pay, gross_pay


# Assigned to Willie Jones
def calculate_net_pay(gross_pay: float) -> float:
    state_tax_deduction = STATE_TAX * gross_pay
    federal_tax_deduction = FEDERAL_TAX * gross_pay
    net_pay = round(gross_pay - state_tax_deduction - federal_tax_deduction, 2)
    return state_tax_deduction, federal_tax_deduction, net_pay


# Assigned to Kevin White // Completed by Tyler Howard
# Record FirstName, LastName, EmployeeID, NumDependents, HoursWorked, GrossPay, NetPay
def record_results(data: list) -> None:
    column_headers: list = ["EmployeeID","FirstName","LastName","NumDependents","HoursWorked","PayRate","StandardHours","OvertimeHours","StandardPay","OvertimePay","GrossPay","StateTax","FedTax","NetPay"]
    results_table = pd.DataFrame([data], columns=column_headers)
    results_table.to_csv("results.csv", mode="a", index=False, header=False)

# Run the program only when this script is executed directly
if __name__ == "__main__":
    main()
