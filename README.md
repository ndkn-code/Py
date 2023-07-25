 

Final Project


Objective:

This is a Python project that implements a financial calculator. The calculator allows the user to perform four financial calculations: simple interest, compound interest, present value, and future value. The output will be displayed as a graph, and will be saved to a csv file.





Goal:

The goal of this project is to create a financial calculator that allows for calculating finance related calculations. Belows are the structured of the programs:

The programs ask what calculations the user want it to perform
The user provides input necessary for the corresponding calculations to run
The programs returns the output as a summary followed by a balance accumulation of the corresponding calculations
The programs save the ouput to a csv, including all information along a timestamp
Key functions and methods used in the code:

parse_years: This function takes a string input representing the number of years and converts it into a numeric value in years.

 __init__: This is a constructor method for each of the four calculator classes (SimpleInterestCalculator, CompoundInterestCalculator, PresentValueCalculator, and FutureValueCalculator). It takes in the necessary inputs for the calculation and initializes the object attributes.

main: This is the main function of the script. It prompts the user to select a type of calculation and prompts the user for the necessary inputs for that calculation. It then creates an instance of the appropriate calculator class, calls the calculate method to perform the calculation, and displays the results using the display_results method.

display_results: This method prints out a summary of the calculation and saves the results to a CSV file. If the calculation is a compound interest calculation, it also plots the balance accumulation over time using matplotlib.

calculate: This method performs the financial calculation based on the inputs provided to the constructor and returns the result.

The code also uses several built-in Python functions such as float(), int(), round(), and csv.writer(). Additionally, it uses the matplotlib.pyplot library for plotting the balance accumulation over time for compound interest calculations.


Summary output:



Plot output using matplotlib.pyplot:


CSV file output:



Conclusion:

Overall, this project helps calculate the four financially related calculations and provides plot visualization as well as information output to a csv file.

Github link:






