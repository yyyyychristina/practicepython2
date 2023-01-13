import csv

name = input()

with open(name) as csvfile:
    words = csv.reader(csvfile)
    for j in words:                             
        row = j                                             #assign content with row
        
    tmp = []
    frequencies = 1
    for i in row:                           #for loop in the row
        if i not in tmp:                    #put ONLY THE FIRST TIME OCCURED i into tmp list
            tmp.append(i)
    

    for i in tmp:
        print(i, row.count(i))         #print ONLY THE FIRST TIME OCCURED i and count i in the row list
    
