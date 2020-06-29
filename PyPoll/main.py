#import dependencies (os, csv)
import csv
import os
#tell python where the csv is coming from
election_input = os.path.join("C:/Users/annel/Desktop/python-challenge/PyPoll/Resources/election_data.csv")
#go ahead and set the output filepath too
election_output = os.path.join("C:/Users/annel/Desktop/python-challenge/PyPoll/Analysis/election_results.txt")
#set up the variables: running total of votes cast, list of candidates, and total number of votes per candidate
total_votes=0
candidate_list=[]
candidate_vote_count={}
#variables for the winner
winner="" #who knows
winner_count=0
#read in the election data as a dictionary (So I don't have to skip rows and it knows what everything is. Whoever invented this is a genius.)
with open(election_input) as election_data:
    csv_reader=csv.DictReader(election_data)
    # loop through the rows counting the votes cast at all and the number of votes for each candidate 
    for row in csv_reader:
        total_votes=total_votes+1
        #what candidate is being voted for?
        name=(row["Candidate"])
         #add any new candidates to the total list
        if name not in candidate_list:
            candidate_list.append(name)
            #specifying we're adding to THIS NEW candidate's count
            candidate_vote_count[name]=0 
        #add the vote to this candidate's vote count
        candidate_vote_count[name]=candidate_vote_count[name]+1 
election_rs_pt1=(f"\n-----------------------------\n"
f"Election Results\n"
f"-----------------------------\n"
f"Total Votes Cast: {total_votes}\n"
f"-----------------------------\n")
print(election_rs_pt1)
# then calculate  percentage of the vote per candidate and the winner based on the popular votes (aka, who had the highest percentage)
with open(election_output, "w") as txtfile:
    txtfile.write(election_rs_pt1) #don't need to loop this, so adding it here before I forget.
    for candidate in candidate_vote_count:
        votes=candidate_vote_count.get(candidate)
        share_of_votes= float(votes)/float(total_votes)*100
        candidate_rs= f"{candidate}: {share_of_votes:.2f}% ({votes})\n"
        print(candidate_rs)
        txtfile.write(candidate_rs) #so it prints EVERY candidate instead of just the last one.
        #this is where we find the winner!!!!
        if (votes>winner_count):
            winner_count=votes
            winner=candidate

#then print results in the terminal and in a separate text file.

    election_rs_pt2=(
    f"-----------------------------\n"
    f"Winner: {winner}" 
    f"-----------------------------\n")
    txtfile.write(election_rs_pt2)

print(election_rs_pt2)
