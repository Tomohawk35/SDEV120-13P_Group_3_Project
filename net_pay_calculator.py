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
    # load and store the employee rates table for use in other functions
    rate_table: pd.DataFrame = connect_db()

    global enter_data

    # create loop to continue entering data
    while enter_data == True:

        pay_stub_data: list = []

        # Gather employee data
        employee_id = get_employee_id(rate_table)
        pay_stub_data.append(employee_id)

        first_name, last_name, dependents, hours_worked = input_employee_data()
        pay_stub_data.append(first_name)
        pay_stub_data.append(last_name)
        pay_stub_data.append(dependents)
        pay_stub_data.append(hours_worked)

        # Query table for pay rate
        pay_rate = get_pay_rate(employee_id, rate_table)
        pay_stub_data.append(pay_rate)

        # Calculate gross pay
        standard_hours, overtime_hours, standard_pay, overtime_pay, gross_pay = calculate_gross_pay(hours_worked, pay_rate)
        pay_stub_data.append(standard_hours)
        pay_stub_data.append(overtime_hours)
        pay_stub_data.append(standard_pay)
        pay_stub_data.append(overtime_pay)
        pay_stub_data.append(gross_pay)

        # Calculate net pay
        state_tax_ded, fed_tax_ded, net_pay = calculate_net_pay(gross_pay)
        pay_stub_data.append(state_tax_ded)
        pay_stub_data.append(fed_tax_ded)
        pay_stub_data.append(net_pay)

        record_results(pay_stub_data)
        
        value: str = do_continue()
        while value != "y" and value != "n":
            value = do_continue()
        
        if value == "n":
            enter_data = False
        
    print("Program complete.")


def do_continue():
    return input("Would you like to input more data? (y/n): ")


# Assigned to Fatimatou Ibrahim
def get_employee_id(emp_list: pd.DataFrame) -> int:
    # Prompt and validate employee ID
    while True:
        try:
            e_id: int = int(input("Enter Employee ID: ").strip())
            if e_id not in emp_list.index:
                print(f"Employee ID {e_id} not found in database. Try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer for Employee ID.")
    
    return e_id



def input_employee_data() -> Tuple[str, str, int, float]:
    """
    Prompts the user for employee data, validates employee_id using the database,
    and returns the collected data in a dictionary.
    """

    # Prompt for other details
    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()

    while True:
        try:
            dependents = int(input("Enter Number of Dependents: "))
            if dependents < 0:
                print("Dependents cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for dependents.")

    while True:
        try:
            hours_worked = float(input("Enter Hours Worked: "))
            if hours_worked < 0:
                print("Hours worked cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for hours worked.")
    
    return first_name, last_name, dependents, hours_worked


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
def calculate_gross_pay(hours_worked: float, pay_rate: float) -> float:
    standard_hours: float = min(hours_worked, 40) 
    overtime_hours: float = max(hours_worked - 40, 0) 
    standard_pay: float = round(standard_hours * pay_rate, 2)
    overtime_pay: float = round(overtime_hours * pay_rate * 1.5, 2)
    gross_pay: float = standard_pay + overtime_pay
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


main()