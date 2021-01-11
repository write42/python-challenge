import os
import csv
bank_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
num_rows = 0

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader) 
    total_profit = 0
    max_profit, min_profit = [], []
    for row in csvreader:
        num_rows +=1
        date = row[0]
        #print(" ~ file: main.py ~ line 40 ~ row", row)     
        # print("~ file:main.py ~ line 6 ~ banks",banks)
        total_profit += float(row[1])
        #print(total_profit)
        profit_avg = total_profit/num_rows
        #print(profit_avg)
        #print(num_rows)
        max_profit.append(row[1])
        min_profit.append(row[1])

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {num_rows}")
print(f"Total: {total_profit}")
print(f"Average Change: {profit_avg}")
print(f"Greatest Increase in Profits: {max(max_profit)}")
print(f"Greatest Decrease in Profits: {min(min_profit)}")
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