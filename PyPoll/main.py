import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

#Create Lists to store data
votes = []
candidates =[]
votes_per_candidate = []
winner =[]
percentage =[]
names = []

#Set Up Output print area
print("Election Results")
print(" ")
print("-----------------------------")
print(" ")

#Calculate total number of votes by counting the lines
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #skip header row
    next(csv_reader)
    data = list(csv_reader)
    line_count = len(data)


#Print Number of months
print(f'Total Votes: {line_count} ')
print(" ")
print("-----------------------------")
print(" ")


#Identify each unique candidate
for i in range(0, line_count):
    candidates = data[i][2]
    votes_per_candidate.append(candidates)
    if candidates not in names:
        names.append(candidates)
names = len(candidates)
  
#Calculate total number of votes for each candidate
#for i in range(0, names)
    
