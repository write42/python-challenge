import os
import csv
bank_csv = os.path.join('..','Resources','03-Python_Homework_Instruction_PyBank_Resources_budget_data')

def budget(banks):
    months = banks[0]
    profit = float(banks[1])

    total_months += months 
    total_profit += profit 
    profit_avg = total_profit/total_months
    profit_inc =
    profit_dec = 
    return

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        budget()