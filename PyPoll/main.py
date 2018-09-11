import os
import csv
csvpath = os.path.join('', 'Resources', 'election_data.csv')

#Creates dictionary to be used for candidate name and vote count.
poll = {}

#Sets variable for count
total_votes = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    #creates dictionary from file using column 3 as keys, using each name only once.
    for row in csvreader:
        #counts votes for each candidate as entries
        total_votes += 1
        if row[2] in poll.keys():
            #keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

#create empty list for canditates and his/her vote counts
candidates = []
num_votes = []

#takes dictionary keys and values and, respectively, dumps them into the lists,
# candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

#creates vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#prints to file
output_file = os.path.join("election_results.txt")

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) +
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())
