import csv
import os

OUT_PATH = "election_data_hw.csv"

path = os.path.join("Resources", "election_data.csv")

cand_list = {}

#reading step
with open(path, "r") as file:
    poll_data = csv.DictReader(file)

    data = list(poll_data)
    #gets me my data; creates a list of ordered dictionaries

    #write step
with open(OUT_PATH, "w+") as file:
    
    data_writer = csv.DictWriter(file, ["Voter ID", "County", "Candidate"])
    
    for row in data:
        row = dict(row)
        #changes ordered dict. to the dict we are used to seeing
        
        if row['Candidate'] not in cand_list:
            cand_list[row['Candidate']] = [row['Candidate']].count('candidate') 
        #this creates new dictionay cand_list with Key and values the same:{'Khan': ['Khan'], 'Correy': ['Correy'], 'Li': ['Li'], "O'Tooley": ["O'Tooley"]}
       # else: 
       #     cand_list[row['Candidate']] = 1
             
print(cand_list)


        #total_votes = row[]
        #row["key"] = value
        #add a new key value pair in a regular dict
        
 

        
#percentage of votes of each candidate
#total number of votes of each candidate
#winner of the election
#total number of votes 
#compile list of candidates who received a vote 
#think we do that by creating a new list, iterating over the rows, and adding someone to it with a count and if its already there then just add the count 

