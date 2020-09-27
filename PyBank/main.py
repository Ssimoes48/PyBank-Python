import os
import csv

#Add Path to CSV file 
budget_data = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Set Varriables
total_months = 0
net_profit = 0
change = {}

#Open CVS to make sure it works and print headers
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv.header = next(csvreader)

    #print(f"CSV Header: {csv.header}")

    for row in csvreader:
      total_months += 1
      net_profit += int(row[1])
       
      if total_months == 1:
         prev_month = int(row[1])
      else:
         current_change = int(row[1]) - prev_month
         prev_month = int(row[1])
         change[row[0]] = current_change

average_change = sum(change.values()) / len(change.keys())  
greatest_increase_month = "-20".join(max(change, key=change.get).split('-'))
greatest_decrease_month = "-20".join(min(change, key=change.get).split('-'))
greatest_increase = f"{greatest_increase_month} (${max(change.values())})"  
greatest_decrease = f"{greatest_decrease_month} (${min(change.values())})"  


#Print Results as String Variable
results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_profit:,.2f}
Average Change: ${average_change:,.2f}
Greatest Increase in Profits: {greatest_increase}
Greatest Decrease in Profits: {greatest_decrease}"""

print(results)



output_path = os.path.join('..', 'PyBank', 'Analysis',"PyBank_Results.txt")

#  Open the output file
with open(output_path, "w") as output_file:
   # write
   output_file.write(results)

    # Write in zipped rows
   #writer.writerows(cleaned_csv)