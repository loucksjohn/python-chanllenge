import os
import csv

election_csv = os.path.join('Resources','election_data.csv')

total_votes = []
candidates = []
candidate_vote= {}


# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        candidate_name=row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_vote[candidate_name]=0
        candidate_vote[candidate_name] += 1
        


        

# create list of unique candidates
    # have a counter for each time candidate's name appears?
#
# vote_percent (votes per candidate / total votes) *100

# Print out the anaylsis
    print ("Election Results")
    print ("-----------------------------") 
    print (candidates)
#output print data to text file