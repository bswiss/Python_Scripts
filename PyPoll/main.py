'''Python script to analyze poll data based on a "Voter ID", "County", "Candidate" input csv data structure. The script will:
- read in the input csv file
- print the results to the terminal
- export a text file with the results '''

import csv
import os

csvpath = os.path.join("..", "..", "Input", "election_data_1.csv")

#Read in the data file
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    #Skip header descriptions
    next(csv_reader)

    voter_ID = []
    county = []
    candidate = []
    
    #create separate lists for Voter ID, County and Candidate in empty lists above
    for row in csv_reader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    #Print results for total votes cast
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + str(len(voter_ID)))
    print("-----------------------------")

    candidate.sort()
    candidate_names = []
    votes = []

    from collections import Counter

    #use the counter function to sum the sorted candidate list by name and return dictionary
    c = Counter(candidate)
    
    #from dictionary append the counted votes to the empty votes list
    #from dictionary append the candidates to the empty names list
    for keys, values in c.items():
        votes.append(values)
        candidate_names.append(keys)

    #Use the two list to print the candidate and corresponding % of total votes and vote count
    for i in range(0, len(candidate_names)):
        print(candidate_names[i] + ": " + str(round(100*(votes[i]/len(voter_ID)), 2)) + "% " + "(" + str(votes[i]) + ")")

    #formatting
    print("-----------------------------")

    #Find the winning vote total
    max_votes = max(votes)

    #Loop to find winning candidate name based on winning vote total
    for j in range(0, len(votes)):
        if max_votes == votes[j]:
            print("Winner: " + candidate_names[j])

    print("-----------------------------")

    #write results to a text file
    with open("voting_results.txt", 'w') as results:
        csv_writer1 = csv.writer(results, lineterminator='\n')

        csv_writer1.writerow(["Election Results"])
        csv_writer1.writerow(["-----------------------------"])
        csv_writer1.writerow(["Total Votes: " + str(len(voter_ID))])
        csv_writer1.writerow(["-----------------------------"])

        for i in range(0, len(candidate_names)):
            csv_writer1.writerow([candidate_names[i] + ": " + str(round(100*(votes[i]/len(voter_ID)), 2)) + "% " + "(" + str(votes[i]) + ")"])

        csv_writer1.writerow(["-----------------------------"])

        for j in range(0, len(votes)):
            if max_votes == votes[j]:
                csv_writer1.writerow(["Winner: " + candidate_names[j]])

        csv_writer1.writerow(["-----------------------------"])
        