import csv
import os

OUT_PATH = "budget_data.csv"

path = os.path.join("Resources", "budget_data.csv")

with open(path, "r") as file:
    
    csv_reader = csv.DictReader(file)
#     csv_header = next(csv_reader)
    data = list(csv_reader)
    
    total_months = len(list(data))

#variables (start at 0)
# months = []
prof_loss = 0
avg_change_pl = 0
greatest_increase = 0
greatest_deacrease = 0
total_pl = 0

#print(data)

for row in data:
    row = dict(row)
    #prior_pl = prof_loss
    pl = int(row["Profit/Losses"])
    total_pl += pl 

format_total_pl = "${:,.2f}".format(total_pl)    

with open("Analysis/PyBank.txt", "w+") as file:
    file.write("Financial Analysis\n")
    file.write("______________________________\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: {format_total_pl}\n")
    file.write(f"Average Change: \n")
    file.write(f"Greatest Increase in Profits: \n")
    file.write(f"Greatest Decrease in Profits: \n")
    
    
    
       
        
        
    
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total P/L: {format_total_pl}")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decreae in Profits: ")