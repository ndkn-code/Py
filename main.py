
import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

class SimpleInterestCalculator:
    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate
        self.years = years
        self.balance_accumulation = None

    def calculate(self):
        total_interest = self.principal * self.rate * self.years / 100
        total = round(self.principal + total_interest, 2)
        return total, round(total_interest, 2)

    def display_results(self):
        result, total_interest = self.calculate()
        print("Calculation Summary:")
        print(f"Type: Simple Interest")
        print(f"Principal: {self.principal}")
        print(f"Rate: {self.rate}%")
        print(f"Time: {self.years} year{'s' if self.years > 1 else ''}")
        print(f"Total Amount: {result}")
        print(f"Total Interest: {total_interest}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('finance_calculator_results.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, "Simple Interest", self.principal, self.rate, self.years, result, total_interest])

        if self.balance_accumulation is not None:
            plt.plot(np.arange(len(self.balance_accumulation)), self.balance_accumulation)
            plt.xlabel('Time (Years)')
            plt.ylabel('Balance')
            plt.title('Balance Accumulation')
            plt.show()
        else:
            print("Balance accumulation data is not available.")

class CompoundInterestCalculator:
    def __init__(self, principal, rate, years, frequency):
        self.principal = principal
        self.rate = rate
        self.years = years
        self.frequency = frequency
        self.balance_accumulation = None

    def calculate(self):
        periods = self.years
        rate_per_period = self.rate


        factor = 1 + rate_per_period / 100
        amount = self.principal * pow(factor, periods)
        total_interest = amount - self.principal

        # Calculate balance accumulation
        self.balance_accumulation = [self.principal]
        for _ in range(int(periods)):
            self.balance_accumulation.append(self.balance_accumulation[-1] * factor)

        return round(amount, 2), round(total_interest, 2)

    def display_results(self):
        result, total_interest = self.calculate()
        print("Calculation Summary:")
        print(f"Type: Compound Interest")
        print(f"Principal: {self.principal}")
        print(f"Rate: {self.rate}%")
        print(f"Time: {self.years} year{'s' if self.years > 1 else ''}")
        print(f"Total Amount: {result}")
        print(f"Total Interest: {total_interest}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('finance_calculator_results.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, "Compound Interest", self.principal, self.rate, self.years, result, total_interest, self.frequency])

        if self.balance_accumulation is not None:
            plt.plot(np.arange(len(self.balance_accumulation)), self.balance_accumulation)
            plt.xlabel('Time (Periods)')
            plt.ylabel('Balance')
            plt.title('Balance Accumulation')
            plt.show()
        else:
            print("Balance accumulation data is not available.")

class PresentValueCalculator:
    def __init__(self, future_value, rate, years):
        self.future_value = future_value
        self.rate = rate
        self.years = years
        self.balance_accumulation = None

    def calculate(self):
        present_value = self.future_value / (1 + self.rate / 100) ** self.years
        total_interest = self.future_value - present_value

        # Calculate balance accumulation
        self.balance_accumulation = [self.future_value]
        factor = 1 / (1 + self.rate / 100)
        for _ in range(int(self.years)):
            self.balance_accumulation.append(self.balance_accumulation[-1] * factor)

        return round(present_value, 2), round(total_interest, 2)

    def display_results(self):
        result, total_interest = self.calculate()
        print("Calculation Summary:")
        print(f"Type: Present Value")
        print(f"Future Value: {self.future_value}")
        print(f"Rate: {self.rate}%")
        print(f"Time: {self.years} year{'s' if self.years > 1 else ''}")
        print(f"Present Value: {result}")
        print(f"Total Interest: {total_interest}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('finance_calculator_results.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, "Future value", self.future_value, self.rate, self.years, result, total_interest])

        if self.balance_accumulation is not None:
            plt.plot(np.arange(self.years, -1, -1), self.balance_accumulation)
            plt.xlabel('Time (Years)')
            plt.ylabel('Balance')
            plt.title('Balance Accumulation')
            plt.show()
        else:
            print("Balance accumulation data is not available.")

class FutureValueCalculator:
    def __init__(self, present_value, rate, years):
        self.present_value = present_value
        self.rate = rate
        self.years = years
        self.balance_accumulation = None

    def calculate(self):
        future_value = self.present_value * (1 + self.rate / 100) ** self.years
        total_interest = future_value - self.present_value

        # Calculate balance accumulation
        self.balance_accumulation = [self.present_value]
        factor = 1 + self.rate / 100
        for _ in range(int(self.years)):
            self.balance_accumulation.append(self.balance_accumulation[-1] * factor)

        return round(future_value, 2), round(total_interest, 2)

    def display_results(self):
        result, total_interest = self.calculate()
        print("Calculation Summary:")
        print(f"Type: Future Value")
        print(f"Present Value: {self.present_value}")
        print(f"Rate: {self.rate}%")
        print(f"Time: {self.years} year{'s' if self.years > 1 else ''}")
        print(f"Future Value: {result}")
        print(f"Total Interest: {total_interest}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('finance_calculator_results.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow(
                [timestamp, "Future value", self.present_value, self.rate, self.years, result, total_interest])

        if self.balance_accumulation is not None:
            plt.plot(np.arange(len(self.balance_accumulation)), self.balance_accumulation)
            plt.xlabel('Time (Years)')
            plt.ylabel('Balance')
            plt.title('Balance Accumulation')
            plt.show()
        else:
            print("Balance accumulation data is not available.")

def parse_years(years_str):
    numeric_value = ''.join(filter(str.isdigit, years_str))
    if not numeric_value:
        raise ValueError("Invalid time input. Please enter a numeric value for the time period.")
    numeric_value = float(numeric_value)

    if 'm' in years_str:
        numeric_value /= 12
    elif 'd' in years_str:
        numeric_value /= 365.25

    return numeric_value


def main():
    print("Welcome to the Financial Calculator!")

    while True:
        print("\nPlease select a calculation:")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Present Value")
        print("4. Future Value")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate: "))
            years = parse_years(input("Enter the number of years: "))


            calculator = SimpleInterestCalculator(principal, rate, years)
            calculator.display_results()


        elif choice == '2':
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate: "))
            years = parse_years(input("Enter the number of years: "))
            frequency = "y"

            calculator = CompoundInterestCalculator(principal, rate, years, frequency)
            calculator.display_results()

        elif choice == '3':
            future_value = float(input("Enter the future value: "))
            rate = float(input("Enter the interest rate: "))
            years = parse_years(input("Enter the number of years: "))

            calculator = PresentValueCalculator(future_value, rate, years)
            calculator.display_results()

        elif choice == '4':
            present_value = float(input("Enter the present value: "))
            rate = float(input("Enter the interest rate: "))
            years = parse_years(input("Enter the number of years: "))

            calculator = FutureValueCalculator(present_value, rate, years)
            calculator.display_results()

        elif choice == '5':
            print("Thank you for using the Financial Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
