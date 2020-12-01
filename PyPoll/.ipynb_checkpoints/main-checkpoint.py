import os
import csv

OUT_PATH = "election_data_hw.csv" 

path = os.path.join("Resources","election_data.csv")

with open(path, "r") as file:
    
    csv_reader = csv.DictReader(file)
    
    data = list(csv_reader)
    
    all_votes = len(list(data))
    
    candidate_name = set()

    Correy = 0
    Li = 0
    OTooley = 0
    Khan = 0
  
    for row in data:
        row = dict (row)
        name = row["Candidate"]
        if name not in candidate_name:
            candidate_name.add(name)
        if name == "Correy":
            Correy += 1
        if name == "Li":
            Li += 1
        if name == "O'Tooley":
            OTooley += 1
        if name == "Khan":
            Khan += 1           
            
percent_kahn = round((Khan/all_votes) * 100 , 3)
percent_correy = round((Correy/all_votes) * 100, 3)
percent_li = round((Li/all_votes) * 100, 3)
percent_otooley = round((OTooley/all_votes) * 100, 3)


print("Election Results")               
print("_____________________________")    
print(f"Total Votes: {all_votes}")
print("_____________________________")
print(f"Khan: {percent_kahn}% ({Khan})")
print(f"Correy: {percent_correy}% ({Correy})")
print(f"Li: {percent_li}% ({Li})")    
print(f"O'Tooley: {percent_otooley}% ({OTooley})")
print("_____________________________")

if Khan == max(Khan, Correy, Li, OTooley):
    print("Winner: Khan")
elif Correy == max(Khan, Correy, Li, OTooley):
    print("Winner: Correy")
elif Li == max(Khan, Correy, Li, OTooley):
    print("Winner: Li")
elif OTooley == max(Khan, Correy, Li, OTooley):
    print("Winner: O'Tooley")
    
with open("Analysis/PyPoll_Results.txt", "w+") as file:
    file.write("Election Results\n")               
    file.write("_____________________________\n")    
    file.write(f"Total Votes: {all_votes}\n")
    file.write("_____________________________\n")
    file.write(f"Khan: {percent_kahn}% ({Khan})\n")
    file.write(f"Correy: {percent_correy}% ({Correy})\n")
    file.write(f"Li: {percent_li}% ({Li})\n")    
    file.write(f"O'Tooley: {percent_otooley}% ({OTooley})\n")
    file.write("_____________________________\n")    
    
    if Khan == max(Khan, Correy, Li, OTooley):
        file.write("Winner: Khan") 
    elif Correy == max(Khan, Correy, Li, OTooley):
        file.write("Winner: Correy")
    elif Li == max(Khan, Correy, Li, OTooley):
        file.write("Winner: Li")
    elif OTooley == max(Khan, Correy, Li, OTooley):
        file.write("Winner: O'Tooley")    
    
