import os
import csv
poll_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
num_rows = 0
khan_count = 0
correy_count = 0
li_count = 0
tooley_count = 0
# def polls(votes):
#     total_votes = num_rows
#     candidate = str(votes[2])
#     khan_votes = 0
#     correy_votes = 0
#     li_votes = 0
#     tooley_votes = 0
#     vote_per = (can_total/total_votes) * 100
#     if candidate =="Khan":
#         khan_votes += 1
#         khan_percent = (khan_votes/total_votes)*100
#     elif candidate =="Correy":
#         correy_votes += 1
#         correy_percent = (correy_votes/total_votes)*100
#     elif candidate == "Li":
#         li_votes += 1
#         li_percent = (li_votes/total_votes)*100
#     elif candidate == "O'Tooley":
#         tooley_votes += 1
#         tooley_percent = (tooley_votes/total_votes)*100  
  
    # print("Election Results")
    # print("-------------------------")
    # print(f"Total Votes: {total_votes}")
    # print("-------------------------")
    # print(f"Khan: {khan_percent}% ({khan_votes})")
    # print(f"Correy: {correy_percent}% ({correy_votes})")
    # print(f"Li: {li_percent}% ({li_votes})")
    # print(f"O'Tooley: {tooley_percent}% ({tooley_votes})")

with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        num_rows +=1
        if row[2] == "Khan":
            khan_count += 1
            khan_percent = (khan_count/num_rows) * 100
        elif row[2] == "Correy":
            correy_count +=1
            correy_percent = (correy_count/num_rows) * 100
        elif row[2] =="Li":
            li_count += 1
            li_percent = (li_count/num_rows) * 100
        elif row[2] == "O'Tooley":
            tooley_count += 1
            tooley_percent = (tooley_count/num_rows) * 100

print("Election Results")
print("----------------------")
print(f"Total Votes: {num_rows}")
print("------------------------")
print(f"Khan: {round(khan_percent,3)}% ({khan_count})")
print(f"Cooley: {round(correy_percent,3)}% ({correy_count})")
print(f"Li: {round(li_percent,3)}% ({li_count})")
print(f"O'Tooley: {round(tooley_percent,3)}% ({tooley_count})")
print("-----------------------------------------------------")