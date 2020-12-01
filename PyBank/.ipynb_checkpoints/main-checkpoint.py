import csv
import os

OUT_PATH = "budget_data.csv"

path = os.path.join("Resources", "budget_data.csv")

with open(path, "r") as file:
    
    csv_reader = csv.DictReader(file)
    data = list(csv_reader)
    
    total_months = len(list(data))

#variables (start at 0)
# months = []
net_prof_loss = []
avg_change_pl = []
greatest_increase = []
greatest_deacrease = []
total_prof_loss =[]


    for row in data:
        row = dict(row)
        #print(row)
        total_prof_loss += int(row["Profit/Losses"])
    
    
    
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}"")
print(f"Average Change: {}")
print(f"Greatest Increase in Profits")
print(f"Greatest Decreae in Profits")