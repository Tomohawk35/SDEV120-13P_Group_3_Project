## Code is intended to calculate net pay for any number of employees and record it in a spreadsheet

# used to manage the database file for pulling pay rates
# more information can be found at https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv
import pandas as pd 


# database where employee pay rates are stored
RATE_TABLE: str = "employee_rates.csv"

# tax rates
STATE_TAX: float = 0.056
FEDERAL_TAX: float = 0.079

# sentinel value
SENTINEL: str = "000"

# while loop control
enter_data: bool = True

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
    # load and store the employee rates table for use in other functions
    rate_table: pd.DataFrame = connect_db()

    # create loop to continue entering data
    while enter_data == True:

        # clear variables so values aren't inadvertently carried to next entry
        first_name = None
        last_name = None
        employee_id = None
        dependents = None
        hours_worked = None
        gross_pay = None
        net_pay = None

        # Gather employee data
        employee_id = get_employee_id(rate_table)
        emp_data: dict = input_employee_data(rate_table)

        # Query table for pay rate
        emp_data['pay_rate'] = get_pay_rate(emp_data['employee_id'], rate_table)

        # Calculate gross pay
        emp_data['gross_pay'] = calculate_gross_pay(emp_data['hours_worked'], emp_data['pay_rate'])

        # Calculate net pay
        emp_data['net_pay'] = calculate_net_pay()

        record_results(emp_data)

    pass


# Assigned to Fatimatou Ibrahim
def get_employee_id(emp_list: pd.DataFrame) -> int:
    # Prompt and validate employee ID
    while True:
        try:
            value = input(f"Enter Employee ID or {SENTINEL} to exit: ")
            if value == SENTINEL:
                enter_data = False
                return 000
            
            e_id = int(value)
            if e_id not in emp_list.index:
                print(f"Employee ID {e_id} not found in database. Try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer for Employee ID.")
    
    return e_id



def input_employee_data(emp_list: pd.DataFrame) -> dict:
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

    return {
        "first_name": first_name,
        "last_name": last_name,
        "employee_id": employee_id,
        "dependents": dependents,
        "hours_worked": hours_worked
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
def calculate_gross_pay(hours_worked: float, pay_rate: float) -> float:
    standard_hours = min(hours_worked, 40) 
    overtime_hours = max(hours_worked - 40, 0) 
    standard_pay = standard_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    return round(standard_pay + overtime_pay, 2)


# Assigned to Willie Jones
def calculate_net_pay(gross_pay: float) -> float:
    state_tax_deduction = STATE_TAX * gross_pay
    federal_tax_deduction = FEDERAL_TAX * gross_pay
    net_pay = round(gross_pay - state_tax_deduction - federal_tax_deduction, 2)
    return net_pay


# Assigned to Kevin White
# Record FirstName, LastName, EmployeeID, NumDependents, HoursWorked, GrossPay, NetPay
def record_results(data: dict) -> None:
    result_data: list = [first_name, last_name, employee_id, dependents, hours_worked, gross_pay, net_pay]
    column_headers: list = ["FirstName","LastName","EmployeeID","NumDependents","HoursWorked","GrossPay","NetPay"]
    results_table = pd.DataFrame([result_data], columns=column_headers)
    results_table.to_csv("results.csv", mode="a", index=False, header=False)




df = connect_db()
get_employee_id(df)