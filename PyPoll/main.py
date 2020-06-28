#import dependencies (os, csv)
import csv
import os
#tell python where the csv is coming from
election_input = os.path.join("C:/Users/annel/Desktop/python-challenge/PyPoll/Resources/election_data.csv")
#go ahead and set the output filepath too
election_output = os.path.join("C:/Users/annel/Desktop/python-challenge/PyPoll/Analysis/election_results.txt")
#set up the variables: running total of votes cast, list of candidates, and total number of votes per candidate
total_votes=0
candidate_list=["Khan","Correy","Li","O'Tooley"]
khan_vote=0
correy_vote=0
li_vote=0
otooley_vote=0

#read in the election data as a dictionary (So I don't have to skip rows and it knows what everything is. Whoever invented this is a genius.)
with open(election_input) as election_data:
    csv_reader=csv.DictReader(election_data)
    # loop through the rows counting the votes cast at all and the number of votes for each candidate 
    for row in csv_reader:
        total_votes=total_votes+1
        if [row["Candidate"]]="Khan":
            khan_vote=khan_vote+1
        if [row["Candidate"]]="Correy":
            correy_vote=correy_vote+1
        if [row["Candidate"]]="Li":
            li_vote=li_vote+1
        if [row["Candidate"]]="O'Tooley":
            otooley_vote=otooley_vote+1
       
# then calculate  percentage of the vote per candidate and the winner based on the popular votes (aka, who had the highest percentage)
khan_perc=(khan_vote/total_votes)*100
correy_perc=(correy_vote/total_votes)*100
li_perc=(li_vote/total_votes)*100
otooley_perc=(otooley_vote/total_votes)*100


#then print results in the terminal and in a separate text file.