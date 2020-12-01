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
avg_change_pl = []
greatest_increase = []
greatest_deacrease = []
total_pl = 0

#print(data)

for row in data:
    row = dict(row)
    #prior_pl = prof_loss
    pl = int(row["Profit/Losses"])
    total_pl += pl 

format_total_pl = "${:,.2f}".format(total_pl)    
    
       
        
        
    
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total P/L: {format_total_pl}")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decreae in Profits: ")