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


#Print the total Number of votes
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

#Print Names and Vote Counts and Percentage to 3 decimal places
for i in range (0, name_count):
    print(f"{name_list[i]}: {percentage[i]: .3%} ({votes[i]:,})")


winner = votes.index(max(votes))
print(" ")
print("-----------------------------")
print(" ")
print(f"Winner: {name_list[winner]}")
print(" ")
print("-----------------------------")

#Create text file
file = open(os.path.join("Analysis", "election_analysis.txt"), "w")
#Write values to text file
file.write ("\nElection Analysis")
file.write("\n  ")
file.write ("\n-------------------------")
file.write("\n  ")
file.write ("\nTotal Votes: " + str(line_count))
file.write("\n  ")
file.write ("\n-------------------------")
file.write("\n  ")
for i in range (0, name_count):
    file.write(f"\n{name_list[i]}: {percentage[i]: .3%} ({votes[i]:,})")
file.write("\n  ")
file.write ("\n-------------------------")
file.write("\n ")
file.write(f"\nWinner: {name_list[winner]}")
file.write("\n  ")
file.write ("\n-------------------------")

#Close text file
file.close()   
