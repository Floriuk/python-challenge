import os, csv
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath, encoding='UTF-8') as csvfile:
    pointer = csv.reader (csvfile)
    print('Election Results')
    print(------------------------)
    next(pointer)
    #Declaring my variables
    sum_votes = 0
    total_votes = []

    for x in pointer:
        voters = x[0]
        total_votes.append(voters)

print("Total votes: "+ str(len(total_votes)))