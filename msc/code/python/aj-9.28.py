import json
import os

# Global directory for data storage
monthly_data = {}

def load_data():
    global monthly_data
    if os.path.exists("Aj_expenses.json"):
        with open("Aj_expenses.json", "r") as file:
            global Aj_expenses
            Aj_expenses = json.load(file)
            monthly_data.update(Aj_expenses)

def save_data():
    with open("Aj_expenses.json", "w") as file:
        json.dump(monthly_data, file, indent=4)

def monthly_planner():
    load_data()  # Load existing data

    print("Hello, my name is Mercy. I am your personal assistant that will assist you with managing your money!\n")

    # Ask for the user's name
    name = input("Please enter your name so that I may address you more formally: ")

    month = input("\nPlease enter the current month: ")

    # Create the month's data if there is no data
    if month not in monthly_data:
        monthly_data[month] = {
            "income": 0.0,
            "fixed_expenses": {
                "Tesla Car Payment due the 26th of every month": 505.00,
                "Best Buy Credit Card last payment Oct 14": 94.00,
                "Paypal Credit payment due 6th of every month": 60.00,
                "Wells Fargo Credit Card": 800.00,
                "Tesla Car Insurance": 140.00,
                "Monthly Budget": 500.00,
            },
            "daily_expenses": []
        }

    # Get the user's monthly income
    try:
        income = float(input("\nPlease enter your monthly income: "))
        monthly_data[month]["income"] = income
    except ValueError:
        print("Invalid number! Please input a valid number for your income.")
        return

    print(f"{name}, thank you for providing that information.\nWe can now start planning your monthly expenses for {month}.\nYour monthly income is ${income:.2f}\n")

    # Display fixed expenses
    print(f"Hey {name}, I compiled a list of your monthly expenses:\n")
    total_fixed_expenses = sum(monthly_data[month]["fixed_expenses"].values())
    for item, amount in monthly_data[month]["fixed_expenses"].items():
        print(f"{item}: ${amount:.2f}")

    # Input daily expenses
    while True:
        add_expense = input("\nWould you like to add a daily expense? (yes/no): ").strip().lower()
        if add_expense == 'yes':
            try:
                expense_description = input("Enter a description of your daily expense: ")
                expense_amount = float(input("Enter the price of your daily expense: "))
                monthly_data[month]["daily_expenses"].append((expense_description, expense_amount))
            except ValueError:
                print("Invalid option! Please enter a valid number for your expense.")
                continue
        elif add_expense == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")

    # Display daily expenses
    print("\nHere are your daily expenses:\n")
    total_daily_expenses = sum(amount for _, amount in monthly_data[month]["daily_expenses"])
    for description, amount in monthly_data[month]["daily_expenses"]:
        print(f"{description}: ${amount:.2f}.")

    # Calculate total expenses and savings
    total_expenses = total_fixed_expenses + total_daily_expenses
    savings = income - total_expenses

    print(f"\nYour total monthly expenses are: ${total_expenses:.2f}.\n")
    print(f"After subtracting your total monthly expenses from your monthly income, your total savings for {month} are ${savings:.2f}.")

    # Yearly savings calculation
    yearly_savings = savings * 12
    print(f"\nIf your monthly savings remain consistent, you will save approximately ${yearly_savings:.2f} in a year.")

    # Ask for a target savings goal
    try:
        target_savings = float(input("\nPlease enter the amount you would like to save by the end of the year: "))
        monthly_required_savings = target_savings / 12
        print(f"To reach your goal of ${target_savings:.2f} by the end of the year, you need to save approximately ${monthly_required_savings:.2f} per month.")
    except ValueError:
        print("Invalid number! Please input a valid number for your target savings.")

    save_data()  # Save before closing the script

monthly_planner()
