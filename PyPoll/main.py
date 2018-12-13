import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
votes = []

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvreader)

	for row in csvreader:
		votes.append(row[2])

totalvotes = (len(votes))
candidates = list(set(votes))
totalcandidates = len((list(set(votes))))

name_counter = {}
for name in votes:
        if name in name_counter:
            name_counter[name] += 1
        else:
            name_counter[name] = 1
            
candidates_sorted = sorted(name_counter, key = name_counter.get, reverse=True)

print(f"Election Results")
print(f"-------------------")
print(f"Total Votes: {totalvotes}")
print(f"-------------------")

percents = []
candidatevotes = []

for i in range(0, totalcandidates):
    votei = votes.count(candidates_sorted[i])
    candidatei = candidates_sorted[i]
    percenti = "%.3f" % ((votei/totalvotes)*100)
    percents.append(percenti)
    candidatevotes.append(votei)
    print(f"{candidatei}: {percenti}% ({votei})")

if candidatevotes[0] == candidatevotes[1]:
    winner = "Tie"
else:
    winner = candidates_sorted[0]

print(f"-------------------")
print(f"Winner: {winner}")
print(f"-------------------")

outputpath = os.path.join("output.txt")

with open(outputpath, 'w', newline='') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\nTotal Votes: " + str(totalvotes)) 
    for i in range(0, totalcandidates):
        txtfile.write("\n" + str(candidates_sorted[i]) +": %" + str(percents[i]) + " (" + str(candidatevotes[i]) +")")
    txtfile.write("\nWinner: " + str(winner))   
    txtfile.close()