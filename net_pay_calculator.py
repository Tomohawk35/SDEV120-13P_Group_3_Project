## Code is intended to calculate net pay for any number of employees and record it in a spreadsheet

# used to manage the database file for pulling pay rates
# more information can be found at https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv
import pandas as pd 


# database where employee pay rates are stored
rate_table: str = "employee_rates.csv"

# tax rates
state_tax: float = 0.056
federal_tax: float = 0.079

# employee data
first_name: str
last_name: str
employee_id: int
dependents: int
hours_worked: float
gross_pay: float
net_pay: float


# Main function is assigned to Ashley Kemp
def main():
    pass


# Assigned to Fatimatou Ibrahim
def input_employee_data() -> dict:
    """
    Prompts the user for employee data, validates employee_id using the database,
    and returns the collected data in a dictionary.
    """
    df = connect_db()

    # Prompt and validate employee ID
    while True:
        try:
            employee_id = int(input("Enter Employee ID: "))
            if employee_id not in df.index:
                print(f"Employee ID {employee_id} not found in database. Try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer for Employee ID.")

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

    return {
        "first_name": first_name,
        "last_name": last_name,
        "employee_id": employee_id,
        "dependents": dependents,
        "hours_worked": hours_worked
    }


# Assigned to Tyler Howard
# The hourly rate should be pulled from a database using the employee ID as the primary key.
def connect_db() -> pd.DataFrame: #TODO: Add try-except block in case connection fails
    # database where employee pay rates are stored
    rate_table: str = "employee_rates.csv"

    # read the csv file and store a dataframe ("table")
    df: pd.DataFrame = pd.read_csv(rate_table, header=0, index_col=0) 
    return df


def get_pay_rate(emp_id: int) -> float: 
    rate: float = 0.0 # locally defined rate variable for storing the value
    # df = pd.read_csv(rate_table, header=0, index_col=0) # reads the csv file and stores a dataframe ("table")
    df = connect_db()
    rate = df['employee_rate'].loc[emp_id] # extracts the rate from the dataframe based on the input employee id
    return rate


# TODO: Need to validate emp_id in case a number is entered that is not in the database. 
# Maybe include this in the input_employee_data function. 

# TODO: create a list of the possible employee_id's to check against when inputting data

# Assigned to DeMishia jackson
def calculate_gross_pay(hours_worked: float, pay_rate: float) -> float:
    standard_hours = MIN(hours_worked, 40) 
    overtime_hours = MAX(hours_worked-40, 0) 
    standard_pay = standard_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    return standard_pay + overtime_pay


# Assigned to Willie Jones
def calculate_taxes():
    pass


# Assigned to Kevin White
# Record FirstName, LastName, EmployeeID, NumDependents, HoursWorked, GrossPay, NetPay
def record_results(data: dict) -> None:
    result_data: list = [first_name, last_name, employee_id, dependents, hours_worked, gross_pay, net_pay]
    column_headers: list = ["FirstName","LastName","EmployeeID","NumDependents","HoursWorked","GrossPay","NetPay"]
    results_table = pd.DataFrame([result_data], columns=column_headers)
    results_table.to_csv("results.csv", mode="a", index=False, header=False)


