import os
import csv
poll_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyPoll_Resources_election_data')

def polls(votes):
    total_votes = num_rows
    candidate = str(votes[2])
    can_total = 
    vote_per = (can_total/total_votes) * 100
    winner =

with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter',')
    csv_header = next(csvreader)
    num_rows = 0
    for row in csvreader:
        num_rows +=1
        polls(row)