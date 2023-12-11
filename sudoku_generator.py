"""
filename: sudoku_generator
Purpose: Generate a sudoku game board that chnges each time
"""
import random

def generate_row(numbers):
    #create my arguments and variables
    array = []
    running = True
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []
    check = []
    #create a loop to create the bord based on two rules
    while running == True:
        if len(array) < 9:
            row = []
            while len(row) < 9:
                #generate random numbers
                generate = random.choice(numbers)
                #check if numbers are valid to make a row based on unique numbersets
                if generate not in row:
                    row.append(generate)
            #check if columns are valid for row generated
            if  row[0] not in c1 and row[1] not in c2 and row[2] not in c3 and row[3] not in c4 and row[4] not in c5 and row[5] not in c6 and row[6] not in c7 and row[7] not in c8 and row[8] not in c9:                
                create_column(row,c1,c2,c3,c4,c5,c6,c7,c8,c9)
                array.append(row)  
        else:
            running = False

    for i in array:
        print(i)

    for index,value in enumerate(c1):
        print(f"{c1[index]} {c2[index]} {c3[index]} {c4[index]} {c5[index]} {c6[index]} {c7[index]} {c8[index]} {c9[index]}")

def create_column(row,c1,c2,c3,c4,c5,c6,c7,c8,c9):
    #generate and fill the lists of the columns for the random numbers generated
    c1.append(row[0])
    c2.append(row[1])
    c3.append(row[2])
    c4.append(row[3])
    c5.append(row[4])
    c6.append(row[5])
    c7.append(row[6])
    c8.append(row[7])
    c9.append(row[8])
    return(c1,c2,c3,c4,c5,c6,c7,c8,c9)


def main():
    #set the main list of numbers for the puzzle
    numbers = [1,2,3,4,5,6,7,8,9]
    generate_row(numbers)

main()