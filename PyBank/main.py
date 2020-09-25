import os
import csv

#Add Path to CSV file 
budget_data = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Open CVS to make sure it works and print headers
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv.header = next(csvreader)

    print(f"CSV Header: {csv.header}")

#Set Varriables
Total_Month = -1
Net_Profit = 0
Average_Change = [0]
Greatest_Increase = " "
Greatest_Decrease = " "

for row in open(budget_data):
    Total_Month += 1
    #Net_Profit += int(row[1])


#Print Results
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", + Total_Month)
#print("Total: ", + Net_Profit)
#print("Average Change: ", (Average_Change)
#print("Greatest Increase in Profits: ", + Greatest_Increase)
#print("Greatest Decrease in Profits: ", + Greatest_Decrease)


#output_file = os.path.join('..', 'PyBank', 'Analysis',"PyBank_Results.txt")

#  Open the output file
#with open(output_file, "w") as datafile:
   # writer = csv.writer(datafile)

    # test write
   # writer.writerow("test")

    # Write in zipped rows
    #writer.writerows(cleaned_csv)