## Code is intended to calculate net pay for any number of employees and record it in a spreadsheet

# used to manage the database file for pulling pay rates
# more information can be found at https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv
import pandas as pd 


# database where employee pay rates are stored
rate_table: str = "employee_rates.csv"

# tax rates
state_tax: float = 0.056
federal_tax: float = 0.079


# Main function is assigned to Ashley Kemp
def main():
    pass


# Assigned to Fatimatou Ibrahim
def input_employee_data():
    pass

# Assigned to Tyler Howard
# The hourly rate should be pulled from a database using the employee ID as the primary key.
def get_pay_rate(emp_id: int) -> float:
    rate: float = 0.0 # locally defined rate variable for storing the value
    df = pd.read_csv(rate_table, header=0, index_col=0) # reads the csv file and stores a dataframe ("table")
    rate = df['employee_rate'].loc[emp_id] # extracts the rate from the dataframe based on the input employee id
    return rate


# Assigned to DeMishia jackson
def calculate_gross_pay():
    pass


# Assigned to Willie Jones
def calculate_taxes():
    pass


# Assigned to Kevin White
def record_results():
    pass

