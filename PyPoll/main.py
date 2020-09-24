import os
import csv

election_data = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv.header = next(csvreader)

    print(f"CSV Header: {csv.header}")


output_file = os.path.join('..', 'PyPoll', 'Analysis',"PyPoll_Results.txt")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # test write
    writer.writerow("test")