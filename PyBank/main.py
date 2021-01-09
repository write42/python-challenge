import os
import csv
bank_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

def budget(banks):
    months = str(banks[0])
    profit = float(banks[1])
    profit_inc = 0
    profit_dec = 0

    total_months = num_rows 
    total_profit = sum(profit for r in csv.reader(csv_header)) 
    profit_avg = total_profit/total_months

    for line in banks:
        if profit > profit_inc:
           profit_inc= profit
        if profit < profit_dec:
            profit_dec =profit

    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_profit}")
    print(f"Average change: {profit_avg}")
    print(f"Greatest Increase in Profits: {months} ({profit_inc})")
    print(f"Greatest Decrease in Profits: {months} ({profit_dec})") 
return

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader) 
    num_rows=0
    for row in csvreader:
        num_rows +=1
        budget(row)