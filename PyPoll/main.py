import os
import csv
poll_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

def polls(votes):
    total_votes = num_rows
    candidate = str(votes[2])
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    tooley_votes = 0
    #vote_per = (can_total/total_votes) * 100
    if candidate =="Khan":
        khan_votes += 1
        khan_percent = (khan_votes/total_votes)*100
    elif candidate =="Correy":
        correy_votes += 1
        correy_percent = (correy_votes/total_votes)*100
    elif candidate == "Li":
        li_votes += 1
        li_percent = (li_votes/total_votes)*100
    elif candidate == "O'Tooley":
        tooley_votes += 1
        tooley_percent = (tooley_votes/total_votes)*100  
  
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"Khan: {khan_percent}% ({khan_votes})")
    print(f"Correy: {correy_percent}% ({correy_votes})")
    print(f"Li: {li_percent}% ({li_votes})")
    print(f"O'Tooley: {tooley_percent}% ({tooley_votes})")


with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    num_rows = 0
    for row in csvreader:
        num_rows +=1
        polls(row)