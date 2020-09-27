#Import os & csv
import os
import csv

#Variables 
total_votes = 0
candidate_votes = dict()
results = str()


#Add Path to CSV file 
election_data = os.path.join('Resources', 'election_data.csv')

#Open CVS to make sure it works and test print headers
csv_file = open(election_data, 'r') 
csvreader = csv.reader(csv_file, delimiter=",")
csv.header = next(csvreader)

#print(f"CSV Header: {csv.header}")

#Calculate total Votes
for row in csvreader:
    total_votes += 1

#if/else - create loop to look through data for unique names to add candidate names to dictonary of names
    if row[2] not in candidate_votes:  
        candidate_votes[row[2]] = 1  
    else:
        candidate_votes[row[2]] += 1 


results = f"""Election Results
--------------------------
Total Votes: {total_votes}
--------------------------
"""
#For Loop to find canidate vote total and percent of vote
for candidate in candidate_votes:
    candidate_total = candidate_votes[candidate]  #number of votes per canidate
    candidate_percent = round((candidate_total / total_votes) * 100, 3)  #percent of votes rounded to 3rd decimal like in instructions
    results += f"{candidate}: {candidate_percent}% ({candidate_total})\n"  #Add each candidate total and percent to results string

winner = max(candidate_votes, key=candidate_votes.get)  #Use dic get function to show parts of key in max value. i.e canidate name

#Add winner to results string
results += f"""--------------------------
Winner: {winner}
--------------------------
"""

#Print the results to the terminal
print(results)

#add path for output file to print results
output_path = os.path.join('..', 'PyPoll', 'Analysis',"PyPoll_Results.txt")

#Open the output file
with open(output_path, "w") as output_file:
   # write to file
   output_file.write((results))
