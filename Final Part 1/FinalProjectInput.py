#Sameerah Mustafa
#1584330
#CIS 2348 Final Project Part 1

#import required modules
import csv
import sys


#read data from a single csv file
def read_csv(filename):
    try:
        #initializing the rows list
        rows = []


        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)


            for row in csvreader:
                rows.append(row)

        return rows
    except:
        print(f"No such file exist with name: {filename}")
        sys.exit()


#Function to read csv files
def read_all_inputs(students_data_filename, gpa_filename, graduation_date_filename):
    #reading students data csv
    students_data = read_csv(students_data_filename)

    #reading gpa data csv
    gpa_data = read_csv(gpa_filename)

    #reading grad date csv
    graduation_date_data = read_csv(graduation_date_filename)

    return students_data, gpa_data, graduation_date_data