import os
import csv

election_csv = os.path.join('Resources','election_data.csv')

votes = []
candidates = []
candidate_votes = {}


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

    print ("Election Results")
    print ("-----------------------------") 
    print (f"Total Votes: {str(total_votes)}")
    print ("-----------------------------") 
    
    sum_votes = sum(candidate_votes.values())
    for key, value in candidate_votes.items():
        pct = round(value * 100.0 / sum_votes)
        print(key,(str(float(pct))+'%'),value)
        

    

    
        
# vote_percent (votes per candidate / total votes) *100

# Print out the anaylsis
    
    #print (results)
  