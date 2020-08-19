import os
import csv

finance_csv = os.path.join('..', 'Resources','budget_data.csv')

# Read in the CSV file
with open(finance_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    date = []
    for row in csvreader:
        date.append(row[0])

    balance = []
    for row in csvreader:
        balance.append(row[1])

    total_months = sum(date)
    total_dollars = sum(balance)



    #total_months = len(date)
    #total = sum(balance)
    #daily_change = (current day - previous day(skipping day 1))
    #average_change = avg(daily_change?)     



# Print out the anaylsis
    print ("Financial Analysis")
    print ("-----------------------------") 
    print(f"Total Months: (str{total_months})")
    print(f"Total: {str(total_dollars)}")
    #(f"Average Change: {str(average_change)}")
    #print(f"Greatest Increase in Profits: {str("date and (amount)")}")
    #print(f"Greatest Decrease in Profits: {str("date and (amount)")}")
