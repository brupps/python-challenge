# Open budget_data.csv
# Calculate Total number of months
#Calculate the changes in profit/loss over entire period and average them
#Greatest increase in profits
#Greatest decrease in profits
#Print results and export to text file

import csv
import os

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

 

