import pandas as pd
import operator
election_data_file = "election_data.csv"

# Read and display the CSV with Pandas
election_data_pd = pd.read_csv(election_data_file)

election_data_table = election_data_pd[["Voter ID", "County", "Candidate"]]


totalVotes = len(election_data_table["Voter ID"])
khanVotes = len(
    election_data_table.loc[election_data_table["Candidate"] == 'Khan'])
correyVotes = len(
    election_data_table.loc[election_data_table["Candidate"] == 'Correy'])
liVotes = len(
    election_data_table.loc[election_data_table["Candidate"] == 'Li'])
tooleyVotes = len(
    election_data_table.loc[election_data_table["Candidate"] == 'O\'Tooley'])
khanVotePercentage = "{:.2%}".format((khanVotes/float(totalVotes)))
correyVotePercentage = "{:.2%}".format((correyVotes/float(totalVotes)))
liVotePercentage = "{:.2%}".format((liVotes/float(totalVotes)))
tooleyVotePercentage = "{:.2%}".format((tooleyVotes/float(totalVotes)))

candidateVotes = {}
candidateVotes['Khan'] = khanVotes
candidateVotes['Correy'] = correyVotes
candidateVotes['Li'] = liVotes
candidateVotes['O\'Tooley'] = tooleyVotes
winner = max(candidateVotes.iteritems(), key=operator.itemgetter(1))[0]
f = open('output.txt', 'w')

f.write("Election Results\n")
f.write("-------------------------")
f.write("\nTotal Votes: " + str(totalVotes))
f.write("\nKhan: " + khanVotePercentage + " (" + str(khanVotes) + ")")
f.write("\nCorrey: " + correyVotePercentage + " (" + str(correyVotes) + ")")
f.write("\nLi: " + liVotePercentage + " (" + str(liVotes) + ")")
f.write("\nO'Tooley: " + tooleyVotePercentage + " (" + str(tooleyVotes) + ")")
f.write("\n-------------------------")
f.write("\nWinner: " + str(winner))
f.write("\n-------------------------")
f = open('output.txt', 'r')
for line in f:
    print(line)

f.close

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
