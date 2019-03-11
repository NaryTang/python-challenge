import os
import csv
import operator #import to use "max"

csvpath = os.path.join('Resources', 'election_data.csv')

#starting vote counter
Total_votes = 0

#creating dictionary
mydictionary ={}

#open csv file
with open(csvpath, encoding='utf8', newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	next(csvreader)

	for row in csvreader:

		#adding to vote counter
		Total_votes += 1

		#creating new keys in dictionary
		if row[2] not in mydictionary.keys():
			mydictionary[row[2]] = 1
		#adding to existing keys in dictionary
		else:
			mydictionary[row[2]] += 1

#print summary format
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_votes}")
print("-------------------------")

#for loop through dictionary
for x in mydictionary:

	print(f"{x}: {round(mydictionary[x]/Total_votes*100,3)}% ({mydictionary[x]})") 

print("-------------------------")
print(f"Winner: {max(mydictionary.items(), key=operator.itemgetter(1))[0]}")
print("-------------------------")

#creating path & txt file name
electiontxtpath = os.path.join('.', 'electiondata.txt')

#conveting to TXT
with open(electiontxtpath, 'w') as txt_writer:

	txt_writer.write("Election Results\n")
	txt_writer.write("-------------------------\n")
	txt_writer.write(f"Total Votes: {Total_votes}\n")
	txt_writer.write("-------------------------\n")

	for x in mydictionary:

		txt_writer.write(f"{x}: {round(mydictionary[x]/Total_votes*100,3)}% ({mydictionary[x]})\n") 

	txt_writer.write("-------------------------\n")
	txt_writer.write(f"Winner: {max(mydictionary.items(), key=operator.itemgetter(1))[0]}\n")
	txt_writer.write("-------------------------\n")