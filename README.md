# Capstone Project: Variables and Control Structures in Python

The objective of this capstone project is to create a finance calculator in Python. It will allow users to calculate the amount of interest they would earn on their investment or the amount they will have to pay on a home loan. This project introduces key Python concepts, such as variables, control structures, exception handling, and basic math operations.

## Objectives

This Python program accomplishes the following:

1. It allows the user to choose which calculation they want to do (either "investment" or "bond").

1. It is unaffected by how the user capitalises their selection (i.e., 'Bond', 'bond', 'BOND' or 'investment', 'Investment', 'INVESTMENT', etc., are all recognized as valid entries). If the user does not enter a valid input, it shows an appropriate error message.

1. If the user selects 'investment', the program prompts the user to: 
    - input the amount of money they are depositing, 
    - the interest rate (as a percentage), 
    - the number of years they plan on investing, and
    - whether they want "simple" or "compound" interest.
    - Depending on the inputs, the program calculates the total amount once the interest has been applied, and prints out the answer.

1. If the user selects 'bond', the program prompts the user to:
    - input the present value of the house, 
    - the interest rate, and
    - the number of months they plan to take to repay the bond.
    - Based on the inputs, the program calculates the amount that the person will have to repay each month and outputs the answer.

The Python script that accomplishes this can be found in the file: [capstone_finance_calculator.py](https://github.com/G-o-r-a-n/Capstone-Variables-Control-Structures/blob/main/capstone_finance_calculator.py)

## Code Structure

The code follows this structure:

- **Import the Required Module**: The Python math module is imported to provide access to mathematical functions required for interest and bond calculations.
- **Display the Calculator Options**: The user is shown the two calculation options: 'Investment' and 'Bond'.
- **Prompt for User Choice**: The user is prompted to choose either 'Investment' or 'Bond'. The user's choice is converted to lowercase to make the comparison case-insensitive. Invalid inputs result in an error message and re-prompting of the user until a valid input is received.
- **Investment Calculations**: If the user chooses 'Investment', the script prompts for the necessary inputs: the amount of money to be invested, the annual interest rate, the investment duration in years, and the type of interest (simple or compound). These inputs are validated to ensure they are positive numerical values. Based on the user's input, the appropriate interest formula is used to calculate the expected return.
- **Bond Calculations**: If the user chooses 'Bond', the script prompts for necessary inputs: the current value of the house, the annual interest rate, and the bond repayment duration in months. These inputs are validated to ensure they are positive numerical values. Then, the bond repayment formula is used to calculate the monthly repayment amount.
- **Display Results**: The calculated return for an 'Investment' or the monthly repayment amount for a 'Bond' is displayed to the user.
- **End of Process**: A thank you message is displayed, indicating the end of the calculation process.

## Usage

To use this script, you need to have Python installed on your system. You can then run the script directly:

```
python capstone_finance_calculator.py
```

Make sure to provide the input as prompted by the script. Note that the annual interest rates and the amount of money are expected to be input as numbers (for instance, 8 instead of 8%). The duration for the investment or bond repayment should be input in years or months, respectively.

### Note

This project is part of a capstone series aimed at introducing key Python concepts such as variables and control structures. It provides a practical example of how these concepts can be used in creating a simple financial calculator.