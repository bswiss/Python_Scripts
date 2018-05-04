'''Python script to analyze a paragraph input csv data structure. The script will:
- read in the input csv file
- assess the paragraph for word count, sentence count, letter count (per word), avg sentence length (in words)
- print results to the terminal
- export a text file with the results'''

import csv
import os

csvpath = os.path.join("..", "..", "Input", "paragraph_1.txt")

#Read in the data file
with open(csvpath, 'r') as textfile:
    paragraph = csv.reader(textfile)

    list1 = []

    #Convert the csv.reader paragraph to a list
    for row in paragraph:
        list1.append(row)

    #Convert the list paragraph to a string
    str1 = ''.join(map(str, list1))
    
    #Loops to format the paragraph by removing special characters and leaving the only the words
    for x in str1:
        if x == "'":
            str2 = str1.replace(x, "")

    for x in str2:
        if x == "[":
            str3 = str2.replace(x, "")

    for x in str3:
        if x == "]":
            str4 = str3.replace(x, "")

    for x in str4:
        if x == ",":
            str5 = str4.replace(x, "")

    #Convert the cleaned paragraph string to a list of individual words used to calculate the results
    words = str5.split()

    let_sum = 0
    
    #sum of letters in the words in the paragraph
    for i in range(len(words)):
        let_sum += len(words[i])

    print("Paragraph Analysis")
    print("------------------")
    print("Approximate Word Count: " + str(len(words)))
    #Count the number of "." in the paragraph string to determine the appoximate sentence count
    print("Approximate Sentence Count: " + str(str5.count(".")))
    print("Average Letter Count: " + str(round(let_sum/len(words), 2)) + " lettetrs per word")
    print("Average Sentence Length: " + str(round(len(words)/str5.count("."), 2)) + " words")

    #write results to a text file
    with open("PyParagraph_results.txt", 'w') as results:
        csv_writer1 = csv.writer(results, lineterminator='\n')

        csv_writer1.writerow(["Paragraph Analysis"])
        csv_writer1.writerow(["------------------"])
        csv_writer1.writerow(["Approximate Word Count: " + str(len(words))])
        csv_writer1.writerow(["Approximate Sentence Count: " + str(str5.count("."))])
        csv_writer1.writerow(["Average Letter Count: " + str(round(let_sum/len(words), 2)) + " lettetrs per word"])
        csv_writer1.writerow(["Average Sentence Length: " + str(round(len(words)/str5.count("."), 2)) + " words"])