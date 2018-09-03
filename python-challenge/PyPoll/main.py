import os
import csv
import pandas as pd 
# Set path for file
budget_csv = os.path.join("..","PyPoll","election.csv")

#Outlining my objectives

#1. calculate the total number of votes cast
totalVotes = 0

#2. A complete list of candidates who received votes

df = pd.read_csv(budget_csv)

clean_df = df.groupby(2)
# Open the CSV
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    # Loop through looking for the video
    for row in csvreader:
        totalVotes += 1
        #print(row[0])  #bad idea - it has a lot of data...        
print(totalVotes)
file = open("summary.txt","w")
file.write("Vote Summary:\n")
file.write("Total Votes cast: " + str(totalVotes))