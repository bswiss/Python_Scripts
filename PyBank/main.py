'''Python script to analyze financial data based on a "date", "revenue" data structure input csv file. The script will:
- read in the input csv file
- print the results to the terminal
- export a text file with the results
- export a new csv file with a new column for "Revenue Change"'''

import csv
import os

csvpath = os.path.join("..", "..", "Input", "budget_data_1.csv")

#Read in the data file
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    #Skip header descriptions
    next(csv_reader)

    date = []
    revenue = []
    rev_change = []
    
    #create separate lists for data and revenue and append in empty lists above
    for row in csv_reader:
        date.append(row[0])
        revenue.append(int(row[1]))

    #Print results for total months and total revenue
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months: " + str(len(date)))
    print("Total Revenue: $" + str(sum(revenue)))

    #Populate a list for monthly change in revenue
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])

    #Calculate and print the average monthly revenue change
    avg_rev_change = round(sum(rev_change)/len(rev_change),2)
    print("Average Revenue Change: $" + str(avg_rev_change))

    maxr = 0
    minr = 0

    #Find the max monthly revenue change
    for j in range(len(rev_change)):
        maxr = max(maxr,rev_change[j])

    #Find the min monthly revenue change
    for k in range(len(rev_change)):
        minr = min(minr,rev_change[k])

    #Print results for max/min monthly revenue change
    print("Greatest Increase in Revenue: " + date[rev_change.index(maxr)+1] + " ($" + str(maxr) + ")")
    print("Greatest Decrease in Revenue: " + date[rev_change.index(minr)+1] + " ($" + str(minr) + ")")

    #write results to a text file
    with open("budget_results.txt", 'w') as results:
        csv_writer1 = csv.writer(results, lineterminator='\n')

        csv_writer1.writerow(["Financial Analysis"])
        csv_writer1.writerow(["-----------------------------"])
        csv_writer1.writerow(["Total Months: " + str(len(date))])
        csv_writer1.writerow(["Total Revenue: $" + str(sum(revenue))])
        csv_writer1.writerow(["Average Revenue Change: $" + str(avg_rev_change)])
        csv_writer1.writerow(["Greatest Increase in Revenue: " + date[rev_change.index(maxr)+1] + " ($" + str(maxr) + ")"])
        csv_writer1.writerow(["Greatest Decrease in Revenue: " + date[rev_change.index(minr)+1] + " ($" + str(minr) + ")"])
    
    #Add a row to rev_change for purposes of writing a new data set
    rev_change.insert(0,"NA")
    #Zip lists together for Date, Revenue and Revenue Change
    updated_budget_data = zip(date, revenue, rev_change)

    #Write a new csv file including monthly revenue change
    with open("updated_budget_data.csv", 'w') as new_file:
        csv_writer2 = csv.writer(new_file, lineterminator='\n')

        csv_writer2.writerow(["Date", "Revenue", "Revenue Change"])

        csv_writer2.writerows(updated_budget_data)