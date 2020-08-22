import os
import csv

election_csv = os.path.join('Resources','election_data.csv')

votes = []
candidates = []
candidate_votes= {}


# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        votes.append(row[0])
        candidate_name=row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] += 1

    total_votes = len(votes)
    
    s = sum(candidate_votes.values())
    for k, v in candidate_votes.items():
        pct = round(v * 100.0 / s)
        print(k,(str(float(pct))+'%'),v)

    
        
# vote_percent (votes per candidate / total votes) *100

# Print out the anaylsis
    print ("Election Results")
    print ("-----------------------------") 
    print (candidates)
    print (total_votes)
    print (candidate_votes)
  