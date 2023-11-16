import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

#Create Lists to store data
votes = []
candidates =[]
votes_per_candidate = []
winner =[]
percentage =[]
name = []
name_list = []

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
    if candidates not in name_list:
        name_list.append(candidates)
name_count = len(name_list)

  
#Calculate total number of votes and percentage of votes for each candidate
for i in range(0, name_count):
    name = name_list[i]
    votes.append(votes_per_candidate.count(name))
    votepercent = votes[i]/line_count
    percentage.append(votepercent)
   # for i in range (0,candidates):
    #    print(f"{candidates[i]}: {percentage[i]: .3% ({votes_per_candidate}[i]:,)}")

winner = votes.index(max(votes))

print(winner)
    
