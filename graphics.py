import math
import csv
import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta

class SimpleInterestCalculator:
    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate
        self.years = years

    def calculate(self):
        total_interest  = self.principal * self.rate * self.years / 100
        return round(self.principal + total_interest , 2), round(total_interest, 2)

class CompoundInterestCalculator:
    def __init__(self, principal, rate, years, frequency):
        self.principal = principal
        self.rate = rate
        self.years = years
        self.frequency = frequency

    def calculate(self):
        if self.frequency == 'd':
            periods = self.years
            rate_per_period = self.rate / 365
        elif self.frequency == 'm':
            periods = self.years / 30.44
            rate_per_period = self.rate / 12
        elif self.frequency == 'y':
            periods = self.years / 365.25
            rate_per_period = self.rate
        else:
            raise ValueError("Invalid frequency. Please enter 'd' for daily, 'm' for monthly, or 'y' for yearly.")

        factor = 1 + rate_per_period / 100
        amount = self.principal * pow(factor, periods)
        total_interest = amount - self.principal
        return round(amount, 2), round(total_interest, 2)

class PresentValueCalculator:
    def __init__(self, future_value, rate, years):
        self.future_value = future_value
        self.rate = rate / 100
        self.years = years

    def calculate(self):
        present_value = self.future_value / ((1 + self.rate) ** self.years)
        total_interest = self.future_value - present_value
        return round(present_value, 2), round(total_interest, 2)

class FutureValueCalculator(PresentValueCalculator):
    def __init__(self, present_value, rate, years):
        self.present_value = present_value
        self.rate = rate / 100
        self.years = years

    def calculate(self):
        future_value = self.present_value * ((1 + self.rate) ** self.years)
        total_interest = future_value - self.present_value
        return round(future_value, 2),  round(total_interest, 2)

def parse_time_string(time_string):
    if re.match(r'^\d+$', time_string):  # Only a number is input, assume it is in years
        time_in_years = int(time_string)
        return timedelta(days=int(time_in_years * 365.25))

    match = re.match(r'^(\d+)(d|y|m)$', time_string)
    if not match:
        raise ValueError("Invalid time input format. Please use format '10d', '12y', or '1m'.")

    time_value = int(match.group(1))
    time_unit = match.group(2)

    if time_unit == 'd':
        return timedelta(days=int(time_value))
    elif time_unit == 'y':
        return timedelta(days=int(time_value * 365.25))
    elif time_unit == 'm':
        return timedelta(days=int(time_value * 30.44))

def main():
    while True:
        print("Select a calculation to perform:")
        print("1. Simple interest")
        print("2. Compound interest")
        print("3. Present value")
        print("4. Future value")
        choice = input("Enter choice (1/2/3/4): ")

        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please enter a valid choice.")
            continue

        if choice == '1':
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter rate: "))
            while True:  # Loop until valid time input is provided
                time_string = input("Enter time: ")
                try:
                    time = parse_time_string(time_string)
                    break
                except ValueError as e:
                    print(str(e))
            frequency = "N/A"
            calculator = SimpleInterestCalculator(principal, rate, time.days / 365.25)
            calculation_type = 'Simple Interest'
            result, total_interest = calculator.calculate()
            summary = f"Calculation Summary:\nType: {calculation_type}\nPrincipal: {principal}\nRate: {rate}%\nTime: "
            years = round(float(time.days / 365), 2)
            summary += f"{years} year{'s' if years > 1 else ''}\n"
            summary += f"Total Amount: {result}\nTotal Interest: {total_interest}"
            print(summary)

        elif choice == '2':
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter rate: "))
            while True:  # Loop until valid time input is provided
                time_string = input("Enter time: ")
                try:
                    time = parse_time_string(time_string)
                    break
                except ValueError as e:
                    print(str(e))
            while True:  # Loop until valid frequency input is provided
                frequency = input("Enter compounding frequency (d/m/y): ")
                if frequency in ['d', 'm', 'y']:
                    break
                else:
                    print("Invalid input. Please enter 'd' for daily, 'm' for monthly, or 'y' for yearly.")
            calculator = CompoundInterestCalculator(principal, rate, time.days / 365.25, frequency)
            calculation_type = 'Compound Interest'
            result, total_interest = calculator.calculate()
            summary = f"Calculation Summary:\nType: {calculation_type}\nPrincipal: {principal}\nRate: {rate}%\nTime: "
            years = round(float(time.days / 365), 2)
            summary += f"{years} year{'s' if years > 1 else ''}\n"
            summary += f"Total Amount: {result}\nTotal Interest: {total_interest}"
            print(summary)
        elif choice == '3':
            principal = None
            time_string = None
            future_value = float(input("Enter future value: "))
            rate = float(input("Enter rate: "))
            years = float(input("Enter number of years: "))
            calculator = PresentValueCalculator(future_value, rate, years)
            calculation_type = 'Present Value'
            result, total_interest = calculator.calculate()
            summary = f"Calculation Summary:\nType: {calculation_type}\nFuture value: {future_value}\nRate: {rate}%\nPeriod: {years}\nPresent Value: {result}\nTotal Interest: {total_interest}"
            print(summary)

        elif choice == '4':
            principal = None
            time_string = None
            present_value = float(input("Enter present value: "))
            rate = float(input("Enter rate: "))
            years = float(input("Enter number of years: "))
            calculator = FutureValueCalculator(present_value, rate, years)
            calculation_type = 'Future Value'
            result, total_interest = calculator.calculate()
            summary = f"Calculation Summary:\nType: {calculation_type}\nStarting Amount: {present_value}\nRate: {rate}%\nPeriod: {years}\nFuture Value: {result}\nTotal Interest: {total_interest}"
            print(summary)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if choice in ['1', '2']:
            with open('finance_calculator_results.csv', mode='a') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, calculation_type, principal, rate, years, result,total_interest, frequency])
        elif choice == '3':
            with open('finance_calculator_results.csv', mode='a') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, calculation_type, future_value, rate, years, result, total_interest])
        else:
            with open('finance_calculator_results.csv', mode='a') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, calculation_type, present_value, rate, years, result, total_interest])
        again = input("Perform another calculation? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == '__main__':
    main()