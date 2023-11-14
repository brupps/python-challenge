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
months = []
profits_losses = []
changes = []

#Set Up Output print area
print("Financial Analysis")
print(" ")
print("-----------------------------")
print(" ")

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    #print(csv_reader)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        months.append(row[0])
        profits_losses.append(int(row[1]))
    
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
#Print Number of months
print(f'Total Months: {line_count} ')
print(" ")


#Calculate the total in $
def csv_total(st):
    total = 0
    with open(st) as a:
        csv_reader = csv.reader(a)
        csv_header = next(csv_reader)

        for line in csv_reader:
            total += int(line[1])
            
    return total
total = csv_total(csvpath)
print(f"Total: ${total}")
print(" ")

#Calculate the average change; first the change between each month then average those values
def csv_total(st):
    total = 0
    with open(st) as a:
        csv_reader = csv.reader(a)
        csv_header = next(csv_reader)

    
for i in range (1, len(months)):
        change = profits_losses[i]-profits_losses[i-1]
        changes.append(change)
        
        average_change = sum(changes)/len(changes)

print(f"Average Change is {average_change:.2f}")
print(" ")

#Calculate the greatest increase and decrease in profits as well as the corresponding dates and print them.
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease)+ 1]

print(f"Greatest Increase in Profits:  {greatest_increase_date} (${greatest_increase}) ")
print(" ")
print(f"Greatest Increase in Profits:  {greatest_decrease_date} (${greatest_decrease}) ")
print(" ")


#Create text file
file = open("main_text.txt", 'w')

#Write values to text file
file.write ("\nTotal Months: " + str(line_count))
file.write ("\nTotal: $" + str(total))
file.write ("\nAverage Change: $" + str(average_change))
file.write ("\nGreatest Increase: $" + str(greatest_increase))
file.write ("\nGreatest Decrease: $" + str(greatest_decrease))

#Close text file
file.close()



