import os
import csv
bank_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
num_rows = 0

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader) 
    total_profit = 0
    #max_profit, min_profit = [], []
    profits = []
    date = []
    profits_change = []
    profit_change = 0
    for row in csvreader:
        num_rows +=1
        date.append(row[0])
        profits.append(float(row[1]))
        #print(" ~ file: main.py ~ line 40 ~ row", row)     
        # print("~ file:main.py ~ line 6 ~ banks",banks)
        #total_profit += float(row[1])
        #print(total_profit)
        #profit_avg = 
        #print(profit_avg)
        #print(profit_avg)
        #print(num_rows)
        #max_profit.append(row[1])
        #min_profit.append(row[1])
    for i in range(1,len(profits)):
        profits_change.append(profits[i]-profits[i-1])
        avg_change = sum(profits_change)/len(profits_change)
        max_avg_change = max(profits_change)
        min_avg_change = min(profits_change)
        max_date = str(date[profits_change.index(max(profits_change))])
        min_date = str(date[profits_change.index(min(profits_change))])


print("Financial Analysis")
print("------------------------")
print(f"Total Months: {num_rows}")
print(f"Total: {sum(profits)}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {max_date} ({max_avg_change})")
print(f"Greatest Decrease in Profits: {min_date} ({min_avg_change})")
    #  for i in csvreader:
    #      print(" ~ file: main.py ~ line 31 ~ i", i)
    #      print(" ~ file: main.py ~ line 33 ~ profit", profit)
    #      print(" ~ file: main.py ~ line 34 ~ profit_inc", profit_inc)

    #      if profit > profit_inc:
    #         profit_inc = profit[i]
    #         increase_month = months[i]
    #      elif profit < profit_dec:
    #         profit_dec = profit[i]
    #         decrease_month = months[i]