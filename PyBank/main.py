#Import os & csv
import os
import csv

#Add Path to CSV file 
budget_data = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Set Variables
total_months = 0
net_profit = 0
change = {}

#Open CVS to make sure it works and test print headers
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv.header = next(csvreader)

    #print(f"CSV Header: {csv.header}")

#calculate Totals- Months and Profit
    for row in csvreader:
      total_months += 1
      net_profit += int(row[1])

#Calulate the change in value from month to month
# if/else in for loop      
      if total_months == 1:
         prev_month = int(row[1])
      else:
         current_change = int(row[1]) - prev_month
         prev_month = int(row[1])
         change[row[0]] = current_change

#calculate balance of totals
average_change = sum(change.values()) / len(change.keys())  

#change date format to have full 4-digit year
greatest_increase_month = "-20".join(max(change, key=change.get).split('-'))
greatest_decrease_month = "-20".join(min(change, key=change.get).split('-'))

#value has 2 parts - month and max
greatest_increase = f"{greatest_increase_month} (${max(change.values())})" 
greatest_decrease = f"{greatest_decrease_month} (${min(change.values())})"    


#Print Results as String Variable
#fix values to print as currency ':,.2f'
#tripple quotes """" prints on multiple lines
results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_profit:,.2f}
Average Change: ${average_change:,.2f}
Greatest Increase in Profits: {greatest_increase}
Greatest Decrease in Profits: {greatest_decrease}"""

print(results)

#add path for output file to print results
output_path = os.path.join('..', 'PyBank', 'Analysis',"PyBank_Results.txt")

#  Open the output file
with open(output_path, "w") as output_file:
   # write to file
   output_file.write(results)

