# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv
from qualifier.utils.fileio import save_as_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!

    is_save_confirm = questionary.confirm("Do you want to save the list of qualifying loans as CSV?").ask()
    
    # if the user chooses yes to save the list as CSV
    if is_save_confirm:

        # check if there are any qualifying lenders in the result, if none found, exit with message
        if len(qualifying_loans) < 1:
            sys.exit("No qualifying lenders found, nothing to save.")

       # else, there are qualifying lenders and user has choosen to save the result, call "save_csv" and ask user for file path 
        else:
            header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
            save_csv(qualifying_loans, header)

    # if the user chooses No to save, exit by calling the function "opt_out_from_saving".
    else:
        opt_out_from_saving()        

    
def is_valid_path(path_to_save):
    """ validates the directory path entered by the user to save CSV file.

    Args: path_to_save: file path entered by user.
    """

    # split the path entered by user using "/"
    path_to_save_tokens = path_to_save.split("/")
    # join the path tokens except the last
    dir_path_to_save = "/".join(path_to_save_tokens[:-1])
    csv_dir_path = Path(dir_path_to_save)
    # check if directory exists
    if not csv_dir_path.exists():
        return "false"
    else:
        return "true"

    
def save_csv(filtered_bank_data, header):

    """ Asks the user to enter path for the location to save the results as CSV file. 
    """

    path_to_save = questionary.text("Please enter file path to save.").ask()

    # validates the path using "is_valid_path" function and saves the file using provided path,
    # prints the message that the results are  successfully saved at the given path.

    if is_valid_path(path_to_save) == "true":
        save_as_csv(path_to_save, filtered_bank_data, header)
        print("Successfully saved results into " + path_to_save)

    # if path is invalid, ask the user to enter correct path by printing message and recalling function "save_csv"   
    else:
        print(f"Oops! Can't find this path: {path_to_save}, Please enter correct path.")
        save_csv(filtered_bank_data, header) 

## function to exit out, if user doesnot want to proceed with saving the results as CSV
def opt_out_from_saving():

    """to exit out, if user doesnot want to proceed with saving the results.
    """

    sys.exit("You entered 'n', not saving as CSV")

def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
