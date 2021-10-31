import gspread 
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """ 
    Get sales fihures inout from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, sperated by commas.")
    print("Example: 30,20,20,10,24,30\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

    sale_data = data_str.split(",")

    validate_data(sale_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises Value Error if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")




get_sales_data()

