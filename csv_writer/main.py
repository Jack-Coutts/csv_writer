import pandas as pd
from pathlib import Path
import os
import sys

# Determine the directory of the executable or script
if getattr(sys, "frozen", False):
    # Running as a PyInstaller bundle
    base_dir = os.path.dirname(sys.executable)
else:
    # Running as a normal script
    base_dir = os.path.dirname(os.path.abspath(__file__))


def create_csv():

    # Get the name of the new csv file
    filename = None
    while filename is None:
        filename = input(
            "Please enter the name of your csv file (without .csv or .tsv): "
        )

    # Check whether we are creating a csv or tsv file
    csv_or_tsv = None
    while csv_or_tsv is None:
        file_type = (
            input("Should the file be a csv or tsv? (c/t): ").strip().lower()
        )
        if file_type == "c":
            csv_or_tsv = ","
        elif file_type == "t":
            csv_or_tsv = "\t"
        else:
            print("Please enter 'c' for csv or 't' for tsv.")

    # Add .csv or .tsv to end of filename
    if csv_or_tsv == ",":
        filename = f"{filename}.csv"
    else:
        filename = f"{filename}.tsv"

    # Get the header values for the new csv file
    header_values = []
    while True:
        header_number = len(header_values) + 1
        header_value = input(
            f"Please provide header number {header_number} (leave blank if no more headers): "
        )
        if not header_value:
            break
        header_values.append(header_value)

    # Create rows of data
    list_of_rows = []
    row_number = 1  # Row zero is the header
    add_row = True
    while add_row:
        row = [
            input(f"Please enter value for row {row_number}, {header}: ")
            for header in header_values
        ]
        list_of_rows.append(row)
        row_number += 1

        # Ask if the user wants to add another row
        while True:
            add_another = (
                input("Do you want to add another row? (y/n): ").strip().lower()
            )
            if add_another == "y":
                break  # Continue to add another row
            elif add_another == "n":
                add_row = False  # Stop adding rows
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    # Turn user input into a dataframe
    dataframe = pd.DataFrame(data=list_of_rows, columns=header_values)

    # Write to csv file
    dataframe.to_csv(
        path_or_buf=os.path.join(base_dir, filename),
        sep=csv_or_tsv,
        header=True,
        index=False,
    )
    print("File created.")


def edit_csv():

    # Get the name of the new csv file and check it exists
    filepath = None
    while filepath is None:
        filepath = Path(
            os.path.join(
                base_dir,
                Path(
                    input(
                        "Please enter the filepath of the file you want to edit: "
                    )
                ),
            )
        )
        if filepath.is_file():  # file exists
            print("File found.")
        else:
            print("File not found.")
            filepath = None

    # Check which delimiter is being used
    if ".tsv" in str(filepath):
        delimiter = "\t"
    else:
        delimiter = ","

    # Read in csv file as a dataframe
    csv_dataframe = None
    while csv_dataframe is None:
        try:
            csv_dataframe = pd.read_csv(
                filepath_or_buffer=filepath, header=0, sep=delimiter
            )
            print("Success reading file.")
            header_values = csv_dataframe.columns.values.tolist()
            print(f"File header: {header_values}")
        except Exception as e:
            print(f"Error reading file. {e}")
            csv_dataframe = None

    # Ask whether they want to change csv or tsv file_type
    csv_or_tsv = None
    while csv_or_tsv is None:
        file_type = (
            input("Do you want to save the file as csv or tsv? (c/t): ")
            .strip()
            .lower()
        )
        if file_type == "c":
            csv_or_tsv = ","
            filepath = Path(str(filepath).replace(".tsv", ".csv"))
        elif file_type == "t":
            csv_or_tsv = "\t"
            filepath = Path(str(filepath).replace(".csv", ".tsv"))

        else:
            print("Please enter 'c' for csv or 't' for tsv.")

    # Start adding rows
    print("NOTE: This program only allows you to add rows to the csv file.")
    print("See the last five rows of the file below:")
    print(f"{csv_dataframe.tail(5)}")
    num_of_existing_rows = csv_dataframe.shape[0]

    # Create rows of data
    list_of_rows = []
    row_number = num_of_existing_rows
    add_row = True
    while add_row:
        row = [
            input(f"Please enter value for row {row_number}, {header}: ")
            for header in header_values
        ]
        list_of_rows.append(row)
        row_number += 1

        # Ask if the user wants to add another row
        while True:
            add_another = (
                input("Do you want to add another row? (y/n): ").strip().lower()
            )
            if add_another == "y":
                break  # Continue to add another row
            elif add_another == "n":
                add_row = False  # Stop adding rows
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    # Append new rows to dataframe
    final_csv_df = pd.concat(
        [
            csv_dataframe,
            pd.DataFrame(list_of_rows, columns=header_values),
        ],
        ignore_index=True,
    )

    # Write to csv file
    final_csv_df.to_csv(
        path_or_buf=filepath, sep=csv_or_tsv, header=True, index=False
    )
    print("File created.")


def create_or_edit_csv():

    while True:

        create = (
            input("Do you want to create a new csv file? (y/n): ")
            .strip()
            .lower()
        )

        if create == "y":
            create_csv()
            break
        elif create == "n":
            edit_csv()
            break
        else:
            print("Please enter y to create a file and n to edit a file!")


def main():

    create_or_edit_csv()


if __name__ == "__main__":
    main()
