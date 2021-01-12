import os
import csv
poll_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
analysis_file = os.path.join('Analysis','PyPoll_analysis.txt')
num_rows = 0

winner = []

with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #candidate_vote = {}
    name_vote = {"Khan":0,"Correy":0,"Li":0,"O'Tooley":0}

    for row in csvreader:
        num_rows +=1

        if row[2] == "Khan":
            name_vote["Khan"] += 1
            khan_percent = (name_vote["Khan"]/num_rows) * 100
        elif row[2] == "Correy":
            name_vote["Correy"] +=1
            correy_percent = (name_vote["Correy"]/num_rows) * 100
        elif row[2] =="Li":
            name_vote["Li"] += 1
            li_percent = (name_vote["Li"]/num_rows) * 100
        elif row[2] == "O'Tooley":
            name_vote["O'Tooley"] += 1
            tooley_percent = (name_vote["O'Tooley"]/num_rows) * 100



report = f"""
Election Results
----------------------
Total Votes: {num_rows}
------------------------
Khan: {round(khan_percent,3)}% ({name_vote['Khan']})
Cooley: {round(correy_percent,3)}% ({name_vote['Correy']})
Li: {round(li_percent,3)}% ({name_vote['Li']})
O'Tooley: {round(tooley_percent,3)}% ({name_vote["O'Tooley"]})
--------------------------
Winner: {max(name_vote,key=name_vote.get)}
--------------------------
"""
# Code in Winner line finds the name with the greatest amounts of votes
#name_vote[] are the counters of each candidate vote
with open(analysis_file,'w') as f:
    f.write(report)