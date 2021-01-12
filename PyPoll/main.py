import os
import csv
poll_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
num_rows = 0
khan_count = 0
correy_count = 0
li_count = 0
tooley_count = 0
winner = []


with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    candidate = []
    candidate_vote = {}
    name_vote = {"Khan":0,"Correy":0,"Li":0,"O'Tooley":0}
    #list out names
    #put everything in a dictionary
    #What should be the keys?
    # Can_win = {"name":candidate,
    #  "vote":{winner}}
    #in dictionary, make key values the candidates names, match to their counts
    #add winner in
    # name_vote ={"khan":khan_count}
    for row in csvreader:
        num_rows +=1
    #     if row[2] not in candidate_vote: 
    #         dict[row[2]] = 0
    #     dict[row[2]] = dict[row[2]] + 1
    # count = [{}]

        if row[2] == "Khan":
            name_vote["Khan"] = name_vote["Khan"] + 1
            khan_percent = (name_vote["Khan"]/num_rows) * 100
            #winner = row[2]
        elif row[2] == "Correy":
            name_vote["Correy"] +=1
            correy_percent = (name_vote["Correy"]/num_rows) * 100
        elif row[2] =="Li":
            name_vote["Li"] += 1
            li_percent = (name_vote["Li"]/num_rows) * 100
        elif row[2] == "O'Tooley":
            name_vote["O'Tooley"] += 1
            tooley_percent = (name_vote["O'Tooley"]/num_rows) * 100
        winner = [khan_count,correy_count,li_count,tooley_count]
        candidate = ["Khan","Correy","Li","O'Tooley"]
    #complete list of candidates
        #In for loop, highlight first name, ignore rest until encounter new name
        #Every count for candidate 
        #How to get winner from dictionary?
        if row[2] not in candidate:
            candidate.append(row[2])
            max_win()
print(max(name_vote,key = name_vote.get))
print(candidate)
print(winner)


    #for i in candidate
    #name_vote = {candidate[i]: winner[i]}
        
        
    #complete list of candidates
        #In for loop, highlight first name, ignore rest until encounter new name
        #Every count for candidate 
        #How to get winner from dictionary?
#         if row[2] not in candidate:
#             candidate.append(row[2])
# print(candidate)
# name_vote = {}
#     for i in candidate
#     name_vote = {candidate[i]: winner[i]}
        

print("Election Results")
print("----------------------")
print(f"Total Votes: {num_rows}")
print("------------------------")
print(f"Khan: {round(khan_percent,3)}% ({khan_count})")
print(f"Cooley: {round(correy_percent,3)}% ({correy_count})")
print(f"Li: {round(li_percent,3)}% ({li_count})")
print(f"O'Tooley: {round(tooley_percent,3)}% ({tooley_count})")
print("--------------------------")
print(f"Winner: {max(name_vote,key=name_vote.get)}")
print("--------------------------")