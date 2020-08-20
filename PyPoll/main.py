import os
import csv

election_csv = os.path.join('Resources','election_data.csv')

total_votes = []
candidates = []



# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        candidates.append(row[2])
        uniq_candidate = set(candidates)


        

# create list of unique candidates
    # have a counter for each time candidate's name appears?
#
# vote_percent (votes per candidate / total votes) *100

