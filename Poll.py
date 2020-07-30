#import os and csv

import os
import csv

#join path
election_data = os.path.join("Resources","election_data.csv")   

#create lists

can_name=[]
can_vote=[]

#variable for number of vote

num_votes=0

#open and read file
with open(election_data,'r') as csvfile:
    csv=csv.reader(csvfile, delimiter=",")
    header= next(csvreader)

    for row in csvreader:

    #add votes toget
    num_vote = num_vote + 1

    #cadidate vote for

    candidate = row[2]

    
    #seperate vote on candidate

    if candidate in can_name:
        candidate_index = cand_name.indec(candidate)
        can_vote[candidate_index]=can_vote[candidate_index]+1
    else
        can_name.append(candidate)
        can_vote.append(1)
    
    #percent value indexes and list 
    voter_stats = []
    most_votes = can_vote[0]
    most_votes_index=0

    #find percent of votes per candidate
    for num in range(len(can_name)):
        percent_voted = round(can_vote[num]/num_vote*100,2)
        voter_stats.append(percent_voted)
        if can_vote[num] > most_votes:
            most_votes = can_votes[num]
            print(most_votes)
            most_votes_index=num
    winner = can_nam[most_votes_index]

    #print results

    print("Election Results")
    print("----------------")
    print(f"Total Votes: {num_vote}")

    #print name, percent, and votes of candidates

    for count in range(len(can_name)):
        print(f" {can_name[num]}: {voter_stats[num]}% ({can_vote[num]})")
    
    #print *drumroll please* winner

    print("----------------")
    print(f"Winner: {winner}")
    print("----------------")

    #text file

    file = open("Analysis/poll_analysis.txt", "w")

    file.write("Election Results" + "\n")

    file.write("-------------------" + "\n")

    file.write("Total Votes: " + str(num_vote) + "\n")

    for count in range(len(can_name)):
        file write(f"{can_name[num]}: {voter_stats[num]}% ({can_vote[num]})" + "\n")
    
    file.write("--------------------")
    file.write(f'Winner:{winner}\n')
    file.write("-------------------" + "\n")

    fil.close()


