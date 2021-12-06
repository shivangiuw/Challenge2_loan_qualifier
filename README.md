# **Loan Qualifier Application**

It is an application which works on python command line interface and enables its users to get a list of qualifying lenders which matches the user's loan requrirement criteria and further save the same easily.
The application works by comparing the `daily_rate_sheet` of loan criteria from various loan providers with the users requirements. To do so, it asks and allows the user to dynamically enter information on requirements and other loan parameters such as: loan amount, credit score,debt etc., and returns a list of qualifying lenders.
The application further gives user, the option to save the resulting list of qualifying lenders(if any) as CSV or opt out.

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
Upon launching the loan qualifier application you will be greeted with the following prompts.

---

## Contributor

UW Fintech Bootcamp team
Shivangi GUpta

---

## License

MIT



