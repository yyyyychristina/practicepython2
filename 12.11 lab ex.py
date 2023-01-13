#variables
my_dict = {}
grades = ''
midterm1 = 0
midterm2 = 0
final = 0
no_of_row = 0
new_data = ''

# TODO: Read a file name from the user and read the tsv file here. 
file_name = input()
import csv
with open(file_name, 'r') as file:
    grades_reader = csv.reader(file, delimiter="\t")
    
    
   
   
# TODO: Compute student grades and exam averages, then output results to a text file here. 
    for row in grades_reader:
        name = ''
        name = row[0] + row[1]                         #name include first and second items of row
        scores = [float(cell) for cell in row[2:]]
        average_scores = sum(scores) / len(scores)     #calculating average
        
        if average_scores >= 90:                       #condition for grades on different average scores
            grades = 'A'
        elif 80 <= average_scores < 90:
            grades = 'B'
        elif 70 <= average_scores < 80:
            grades = 'C'
        elif 60 <= average_scores < 70:
            grades = 'D'
        else:
            grades = 'F'
        row.append(grades)                            #add grades to the end of the row
        
        
        midterm1 += float(row[2])
        midterm2 += float(row[3])
        final += float(row[4])
        
        no_of_row += 1                              #counting no_of_row
        for i in range(len(row)):
            if row[i] == row[-1]:                   #if row[i] is at the end of the row
               break
            new_data += row[i] + "\t"            #i.e. new_data = row[i]   row[i]    
        new_data += row[i] + "\n"                  #i.e. (row[i] is at the end of the row + \n)add to the new_data

            
                
        
    average_midterm1 = midterm1/ no_of_row
    average_midterm2 = midterm2 / no_of_row
    average_final = final / no_of_row
    


    f = open("report.txt", "w")
    f.write(f"{new_data}\n")
    f.write(f"Averages: midterm1 {average_midterm1:.2f}, midterm2 {average_midterm2:.2f}, final {average_final:.2f}\n")
    f.close()
    
