import requests
import re
from datetime import datetime


def get_stock_symbol():
    while True:
        try:
            stock_symbol = input("\nEnter the symbol for the company: ")
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&&apikey=V33ZAOO7VB64CV9C'
            r = requests.get(url)
            
            if is_valid_stock_symbol(stock_symbol):
              if r.status_code == 200:
                  data = r.json()
                  if "Meta Data" in data:
                      print("Symbol found: ", stock_symbol)
                      return stock_symbol
                  else:
                      print("The Stock symbol you inputted does not exist.")
              else:
                  print(f"Error: Request failed with status code {r.status_code}")
            else: 
              print("The Stock symbol you inputted is not valid.")
        except Exception as e:
            print("An error occurred:", e)

def is_valid_stock_symbol(symbol):
  # Validation logic: capitalized, 1-7 alpha characters
  return symbol.isupper() and 1 <= len(symbol) <= 7 and symbol.isalpha()

def get_chart_type():
  print("\n\nCHART TYPES:\n---------------------------\n1. Bar\n2. Line\n\n")
  while(True):
    chart_type = input("Enter the chart type you want (1 or 2): ")
    if is_valid_chart_type(chart_type):
      return chart_type
    else:
      print("\nInvalid entry. Please enter either 1 or 2.\n\n")


def is_valid_chart_type(chart_type):
  return chart_type in ['1', '2']

def get_time_series():
  print("\n\nSelect the time series of the chart you want to generate:\n-----------------------------------------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n\n")
  while(True):
    time_series = input("Enter time series option (1, 2, 3, 4): ")
    if is_valid_time_series(time_series):
      return time_series
    else:
      print("\nInvalid entry. Please enter either 1, 2, 3, or 4.\n\n")


def is_valid_time_series(time_series):
    return time_series in ['1', '2', '3', '4']


def get_start_date():
    while True:
        user_input = input("\n\nEnter the start date (YYYY-MM-DD): ")
        # Use regular expression to validate the input format
        if re.match(r'^\d{4}-\d{2}-\d{2}$', user_input):
            try:
                # Try to parse the input as a date
                date_obj = datetime.strptime(user_input, '%Y-%m-%d')
                if is_valid_date(date_obj):
                  return date_obj
                else:
                   print("Please use a date after the year 1999")
                   
            except ValueError:
                print("Invalid input. Please enter a date in YYYY-MM-DD format.")
                pass  # Invalid date

def is_valid_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj > datetime.strptime("2000-01-01", "%Y-%m-%d")
    except ValueError:
        return False


def get_end_date(start_date):
    while True:
        user_input = input("\n\nEnter the end date (YYYY-MM-DD): ")
        # Use regular expression to validate the input format
        if re.match(r'^\d{4}-\d{2}-\d{2}$', user_input):
            try:
                # Try to parse the input as a date
                date_obj = datetime.strptime(user_input, '%Y-%m-%d')
                # Check if the end date is after the start date
                if is_valid_end_date(date_obj):
                    if(date_obj > (datetime.now())):
                      return date_obj
                    else:
                       print("End date should be before the current date")
                else:
                    print("End date should be after the start date.")
                if date_obj > start_date:
                    return date_obj
                else:
                      print("End date should be after the start date.")
            except ValueError:
                print("Invalid input. Please enter a date in YYYY-MM-DD format.")
                pass  # Invalid date


def is_valid_end_date(start_date_str, end_date_str):
    if not is_valid_date(start_date_str) or not is_valid_date(end_date_str):
        return False
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    return end_date > start_date

def main():
  print("\n\nStock Data Visualizer\n---------------------------")
  stock_symbol = get_stock_symbol()
  chart_type = get_chart_type()
  time_series = get_time_series()
  start_date = get_start_date()
  end_date = get_end_date(start_date)


