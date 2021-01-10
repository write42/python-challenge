import os
import csv
poll_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

def polls(votes):
    total_votes = num_rows
    candidate = str(votes[2])
    #vote_per = (can_total/total_votes) * 100
    if candidate =="Khan":
        print(f"{candidate}: {vote_per}% ()")
    elif candidate =="Correy":
            print(f"{candidate}: {vote_per}% ()")
    elif candidate == "Li":
                print(f"{candidate}: {vote_per}% ()")
    elif candidate == "O'Tooley":
                    print(f"{candidate} :{vote_per}% ()")


with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    num_rows = 0
    for row in csvreader:
        num_rows +=1
        polls(row)