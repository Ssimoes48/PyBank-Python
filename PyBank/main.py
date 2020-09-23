import os
import csv

budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv.header = next(csvreader)

    print(f"CSV Header: {csv.header}")
