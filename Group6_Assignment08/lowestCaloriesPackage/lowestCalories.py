#lowestCalories.py
#Name:Ruolin Chen
#email:chenr9@mail.uc.edu
#Assignment Title: Assignment 08
#Course: IS4010-001
#Semester/Year: Spring 2024
#Brief Description: This module pulls lowest 5 rows from # "rows", sorted by the 5th element(calories), then pulls last two columns of bottom_5_calories
#Citations: https://stackoverflow.com/questions/39511011/lambda-python-function-in-reversing-list
#Anything else that's relevant: 

def getBottom5(rows):

    '''

    takes rows as an argument and pulls the lowest 5 calorie options

    @param rows from data

    @return list of 5 lowest calorie items

    '''

    # Get the lowest 5 rows, lambda tells the function to sort on the fourth column, sorted() defaults to ascending order, also ignores None values

    bottom_5_calories = sorted(rows, key=lambda x: x[4] if x[4] is not None else float('inf'))[:5]

    # this pulls only the product description column of the newly sorted bottom_5_calories list

    return [(row[-2]) for row in bottom_5_calories]