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
        can_vote[candidate_index]=can_vo