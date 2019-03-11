#First we'll import the os module
#This will allow us to create file paths across operating systems
import os
import csv
import operator #import to use "max"

#Path to collect data from Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

#start count number of months
num_of_months = 0

#start total amount of profit/loss over the entire period
total_amount = 0

#calculate the average of the changes in profit/loss over the entire period
#create new list for profit/loss
profit_list = []

#create dictionary to find greatest increase/decrease
mydictionary ={}

#establish previous profit/loss to compare
previousPL = 0

#now you open it...windows users use encoding='utf8' to translate
with open(csvpath, encoding='utf8', newline='') as csvfile: #csvfile is a variable we create a handler (handler is what handles the filer)
	
	#CSV reader specifies delimiter and variable that holds content
	csvreader = csv.reader(csvfile, delimiter=',')

	#skips the header(aka first line)
	next(csvreader)

	#each row is read as a row
	for row in csvreader:
		
		#adding to the counter
		num_of_months +=1

		#adding to the total amount
		total_amount += int(row[1])

		#add to the profit list
		profit_list.append(int(row[1]))

		#adding to the dictionary
		mydictionary.update({row[0]:(int(row[1])-previousPL)})

		#reseting previousPL
		previousPL = int(row[1])

	#calculate the average of the changes in profit/loss over the entire period
	average_change = (profit_list[-1] - profit_list[0])/(num_of_months-1)
	
	print(f"Total Months: {num_of_months}")
	print(f"Total: ${total_amount}")
	print(f"Average Change: ${round(average_change,2)}")
	print(f"Greatest increase in profits: {max(mydictionary.items(), key=operator.itemgetter(1))[0]} (${max(mydictionary.items(), key=operator.itemgetter(1))[1]})")
	print(f"Greatest decrease in profits: {min(mydictionary.items(), key=operator.itemgetter(1))[0]} (${max(mydictionary.items(), key=operator.itemgetter(1))[1]})")

#establish txt path & naming file
datatextpath = os.path.join(".", "budget_data.txt")

#convert to TXT file
with open(datatextpath, 'w') as txt_writer:
	txt_writer.write(f"Total Months: {num_of_months}\n")
	txt_writer.write(f"Total: ${total_amount}\n")
	txt_writer.write(f"Average Change: ${round(average_change,2)}\n")
	txt_writer.write(f"Greatest increase in profits: {max(mydictionary.items(), key=operator.itemgetter(1))[0]} (${max(mydictionary.items(), key=operator.itemgetter(1))[1]})\n")
	txt_writer.write(f"Greatest decrease in profits: {min(mydictionary.items(), key=operator.itemgetter(1))[0]} (${max(mydictionary.items(), key=operator.itemgetter(1))[1]})\n")