import os
import csv

finance_csv = os.path.join('Resources','budget_data.csv')


# Read in the CSV file
with open(finance_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    date = [] 
    balance = []
    average_change = []

    #adding data from rows into date & balance lists
    for row in csvreader:
        date.append(row[0])
        balance.append(int(row[1])) 

    #looping through to get sum of change
    for i in range(len(balance)-1):
        average_change.append(balance[i+1]-balance[i])

    #converting sum of change into avg change
    average_change_total = '${:,.2f}'.format(sum(average_change)/len(average_change))
    
    #setting up variables for printing
    total_months = len(date)
    total_dollars = sum(balance)   
    max_increase = max(average_change)
    min_increase = min(average_change)

    
# Print out the anaylsis
    print ("Financial Analysis")
    print ("-----------------------------") 
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(total_dollars)}")    
    print(f"Average Change: {str(average_change_total)}")
    print(f"Greatest Increase in Profits: $({str(max_increase)})")
    print(f"Greatest Decrease in Profits: $({str(min_increase)})")

#output print data to text file
