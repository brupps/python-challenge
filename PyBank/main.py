# Open budget_data.csv
# Calculate Total number of months
#Calculate the changes in profit/loss over entire period and average them
#Greatest increase in profits
#Greatest decrease in profits
#Print results and export to text file

import csv
import os

csvpath = os.path.join('Resources', 'budget_data.csv')

#Lists to store data
dates = []
profits_losses = []

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")



    months = sum(1 for row in csvreader)
    print("Financial Analysis")
    print(" ")
    print("-----------------------------")
    print(" ")
    print(f"Total Months: {int(months)}")
    print (" ")


#Sum as funciton
def csv_total(st):
    total = 0
    with open(st) as a:
        csvreader = csv.reader(a)
        next(csvreader)
        for line in csvreader:
            total += int(line[1])

    return total

total = csv_total(csvpath)
print(f"Total: ${total}")
print(" ")

#Calculate Average

