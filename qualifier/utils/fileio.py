# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_as_csv(csv_file_path, bank_data, header):
    """writes the CSV file to path entered.

    Args:
        csv_file_path: The csv file path.
        filtered_bank_data: list of qualifying lenders filtered fron bank_data
        header

    Returns:
       rows of the qualifying lenders written in CSV file with headers
    """
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        for row in bank_data:
            writer.writerow(row)    
