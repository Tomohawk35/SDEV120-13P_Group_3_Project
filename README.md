# SDEV120-13P_Group_3_Project
Group 3 Project for SDEV120 at IvyTech
## Team Contributions

**Fatimatou Ibrahim**

- Completed implementation and validation of `input_employee_data` in `net_pay_calculator.py`
- Successfully tested all six test cases using `pytest`
- Resolved setup errors with pip and pytest using a virtual environment
- Collaborated through GitHub, ensured code quality and pushed final updates
- Available for follow-up support if needed

### Command Guide

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate     # On Mac/Linux
# or
venv\Scripts\activate        # On Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest test_cases.py

# Freeze environment (if needed)
pip freeze > requirements.txt

# Deactivate environment (when done)
deactivate
