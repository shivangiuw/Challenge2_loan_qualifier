# **Loan Qualifier Application**

It is an application which works on python command line interface and enables its users to get a list of qualifying lenders which matches the user's loan requrirement criteria and further save the same easily.
The application works by comparing the `daily_rate_sheet` of loan criteria from various loan providers with the users requirements. To do so, it asks and allows the user to dynamically enter information on requirements and other loan parameters such as: loan amount, credit score,debt etc., and returns a list of qualifying lenders.
The application further gives user, the option to save the resulting list of qualifying lenders(if any) as CSV by enabling user to enter the file path or opt out.

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [sys](https://docs.python.org/3/library/sys.html) - For exiting from python at the end of application process

* [path] (https://docs.python.org/3/library/os.path.html) - For CSV file paths to read and write

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
  ```

---

  ## Usage

To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```
Upon launching the loan qualifier application you will be greeted with different prompts to input loan data and options to save
qualifying loans data as CSV by providing file path or optout of the option.


Following are the screenshots of the program run with different user inputs.

* Scenario 1: If there are qualifying loans and user chooses to save file as CSV and provide valid file path
![when user chooses to save list of qualifying loans as CSV and provides valid path](images/successfully_saved_csv.png)
![list of qualifying loans](images/qualifying_loans.png)

* Scenario 2: If there are no qualifying loans for the user
![when there are no qualifying loans](images/no_qualifying_loans.png)

* Scenario 3: If user chooses to save trhe list but provides invalid path
![when user provides invalid file path](images/invalid_file_path.png)

* Scenario 4: If user does not want to save the results of qualifying loans
![when user opts out of saving the list of qualifying loans as CSV](images/user_optout.png)


---

## Contributor

UW Fintech Bootcamp team
Shivangi Gupta

---

## License

MIT



