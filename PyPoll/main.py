import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#opening file as csv
with open(csvpath, encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    next(pointer)
    # Declaring my variables
    total_votes = 0
    sum_votes = 0
    candidate_dict = {}
    candidate_list = []

    #Creating the for loop to start retrieving info
    for x in pointer:
        total_votes += 1
        candidate_name = x[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

            candidate_dict[candidate_name] = 0

        candidate_dict[candidate_name] +=1

#creating my variablles to count the votes for each candidate
charles_votes = candidate_dict["Charles Casper Stockham"]
diana_votes = candidate_dict["Diana DeGette"]
raymon_votes = candidate_dict["Raymon Anthony Doane"]
charles_percentage = charles_votes/total_votes*100
diana_percentage = diana_votes/total_votes*100
raymon_percentage = raymon_votes/total_votes*100

#comparing the votes of each candidate
if charles_percentage > diana_percentage and charles_percentage > raymon_percentage:
    winner = "Charles Casper Stockham"
if diana_percentage > charles_percentage and diana_percentage > raymon_percentage:
    winner = "Diana DeGette"
if raymon_percentage > charles_percentage and raymon_percentage > diana_percentage:
    winner = "Raymon Anthony Doane"
    
#printing results
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {charles_percentage:.3f}% ({charles_votes})
Diana DeGette: {diana_percentage:.3f}% ({diana_votes})
Raymon Anthony Doane: {raymon_percentage:.3f}% ({raymon_votes})
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

#exporting to text file
with open("analysis/pypoll.text", "w") as f:
    f.write(output)
