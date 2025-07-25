## Code is intended to calculate net pay for any number of employees and record it in a spreadsheet

# used to manage the database file for pulling pay rates
# more information can be found at https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv
import pandas as pd 


# database where employee pay rates are stored
rate_table: str = "employee_rates.csv"

# tax rates
STATE_TAX: float = 0.056
FEDERAL_TAX: float = 0.079

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

    # Gather employee data
    emp_data: dict = input_employee_data(rate_table)

    # Query table for pay rate
    emp_data['pay_rate'] = get_pay_rate(emp_data['employee_id'], rate_table)

    # Calculate gross pay
    emp_data['gross_pay'] = calculate_gross_pay(emp_data['hours_worked'], emp_data['pay_rate'])

    # Calculate net pay
    emp_data['net_pay'] = calculate_taxes()

    record_results(emp_data)

    pass


# Assigned to Fatimatou Ibrahim
def input_employee_data(emp_list: pd.DataFrame) -> dict:
    """
    Prompts the user for employee data, validates employee_id using the database,
    and returns the collected data in a dictionary.
    """
    # Prompt and validate employee ID
    while True:
        try:
            employee_id = int(input("Enter Employee ID: "))
            if employee_id not in emp_list.index:
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
def connect_db() -> pd.DataFrame: 
    # database where employee pay rates are stored
    rate_table_file: str = "employee_rates.csv"

    # read the csv file and store a dataframe ("table")
    try:
        rate_data: pd.DataFrame = pd.read_csv(rate_table_file, header=0, index_col=0) 
        return rate_data
    except:
        print(f"Unable to read from {rate_table_file}")


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
def calculate_taxes():
    pass
# start
# define stateTax, federalTax, grossPay, netPay, stateTaxDeduction, federalTaxDeduction, totalTaxDeduction,
# input grossPay = float(input (“Enter Gross Pay:  “))
#      if grossPay >= 0:
#     else:  print(“Gross Pay Cannot Be Negative. Please Enter A Valid Amount.”)
#     except ValueError:
#     print(“Invalid Input. Please Enter A Numeric Value For Gross Pay.”)

# stateTax = .056
# federalTax = .079
# stateTaxDeduction = stateTax * grossPay
# federalTaxDeduction = federalTax * grossPay
# totalTaxDeduction = stateTaxDeduction + federalTaxDeduction
# netPay = grossPay - totalTaxDeduction

# print("Gross Pay: ", grossPay)
# print("State Taxes: ", stateTaxDeduction)
# print("Federal Taxes: ", federalTaxDeduction)
# print("Total Taxes: ", totalTaxDeduction)
# print("Net Pay: ", netPay)
# end

# def calculate_net_pay(gross_pay):
#     stateTax = 0.056
#     federalTax = 0.079
#     stateTaxDeduction = stateTax * gross_pay
#     federalTaxDeduction = federalTax * gross_pay
#     totalTaxDeduction = stateTaxDeduction + federalTaxDeduction
#     netPay = gross_pay - totalTaxDeduction
#     return stateTaxDeduction, federalTaxDeduction, totalTaxDeduction, netPay




# Assigned to Kevin White
# Record FirstName, LastName, EmployeeID, NumDependents, HoursWorked, GrossPay, NetPay
def record_results(data: dict) -> None:
    result_data: list = [first_name, last_name, employee_id, dependents, hours_worked, gross_pay, net_pay]
    column_headers: list = ["FirstName","LastName","EmployeeID","NumDependents","HoursWorked","GrossPay","NetPay"]
    results_table = pd.DataFrame([result_data], columns=column_headers)
    results_table.to_csv("results.csv", mode="a", index=False, header=False)


