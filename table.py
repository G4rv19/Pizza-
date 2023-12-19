import csv
from tabulate import tabulate

try:
    with open("regular.csv", "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    print(tabulate(data, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    print("Error: The specified file 'regular.csv' does not exist.")
except csv.Error as e:
    print(f"Error reading CSV file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
