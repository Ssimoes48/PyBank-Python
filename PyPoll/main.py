import os
import csv

election_data = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv.header = next(csvreader)

    print(f"CSV Header: {csv.header}")
