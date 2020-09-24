import os
import csv

budget_data = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv.header = next(csvreader)

    print(f"CSV Header: {csv.header}")

num_rows = -1

for row in open(budget_data):
    num_rows += 1

print("Total Months: ", + num_rows)




output_file = os.path.join('..', 'PyBank', 'Analysis',"PyBank_Results.txt")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # test write
    writer.writerow("test")

    # Write in zipped rows
    #writer.writerows(cleaned_csv)