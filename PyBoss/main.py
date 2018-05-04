'''Python script to analyze employee data based on a "Emp ID", "Name", "DOB", "SSN", "State" input csv data structure. The script will:
- read in the input csv file
- reformat the data to required specifcations
- export a csv file with the formatted data'''

import csv
import datetime
import os

csvpath = os.path.join("..", "..", "Input", "employee_data1.csv")

#Read in the data file
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    #Skip header descriptions
    next(csv_reader)

    #Create empty lists to fill
    emp_ID = []
    name = []
    DOB = []
    SSN = []
    state = []
    new_state = []

    #create separate lists for current data
    for row in csv_reader:
        emp_ID.append(row[0])
        name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        state.append(row[4])

    #Split name into first and last name and append to new lists
    first_name = [i.split(" ")[0] for i in name]
    last_name = [i.split(" ")[1] for i in name]
    #Update date format and append to new list
    new_DOB = [(datetime.datetime.strptime(i, '%m/%d/%Y').strftime('%m/%d/%Y')) for i in DOB]
    #Append SSN data to new list and format
    SSN1 = [i.split("-")[2] for i in SSN]
    new_SSN = [("***-**-" + i) for i in SSN1]

    #Copy in US State Abbreviation Dictionary
    us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT',
    'Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA',
    'Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN',
    'Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM',
    'New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI',
    'South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA',
    'West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}

    #Find corresponding state abbreviation for current data and append to new list
    for i in state:
        for key, value in us_state_abbrev.items():
            if i == key:
                new_state.append(value)
                break

    #Zip employee ID with all of the new data lists created above
    new_emp_data = zip(emp_ID,first_name,last_name,new_DOB,new_SSN,new_state)

    #Write a new csv file with the new data formats required for the assignment
    with open("updated_employee_data.csv", 'w') as new_file:
        csv_writer2 = csv.writer(new_file, lineterminator='\n')

        csv_writer2.writerow(["Emp ID", "First NAme", "Last Name", "DOB", "SSN", "State"])

        csv_writer2.writerows(new_emp_data)