import os
import csv

#Variables 
Total_Votes = 0
candidate_votes = {}


election_data = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv.header = next(csvreader)

    print(f"CSV Header: {csv.header}")

    for row in csvreader:
        Total_Votes += 1

        if row[2] not in candidate_votes:  
            candidate_votes[row[2]] = 1  
        else:
            candidate_votes[row[2]] += 1

    print(Total_Votes)
    print(candidate_votes)


#output_file = os.path.join('..', 'PyPoll', 'Analysis',"PyPoll_Results.txt")

#  Open the output file
#with open(output_file, "w") as datafile:
    #writer = csv.writer(datafile)

    # test write
    #writer.writerow("test")    