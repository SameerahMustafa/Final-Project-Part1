#Sameerah Mustafa
#1584330
#CIS 2348 Final Project Part 1

#import csv module
import csv


#Define function to csv file
def write_csv(output_filename, rows):
    # writing to csv file
    with open(output_filename, 'w', newline='') as csvfile:
        #create csv writer object
        csvwriter = csv.writer(csvfile)

        #write data rows
        csvwriter.writerows(rows)

    print(f'Data successfully stored in {output_filename}')