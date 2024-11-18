#pyhton program to convert the month name to a number of days.
def days_in_month(month):
    month_days = {
        "January": 31,
        "February": 28,  # Assume non-leap year
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }
    
    return month_days.get(month, "Invalid month name")

# Example usage
month_name = input("Enter the month name: ")
days = days_in_month(month_name)

if isinstance(days, int):
    print(f"{month_name} has {days} days.")
else:
    print(days)
