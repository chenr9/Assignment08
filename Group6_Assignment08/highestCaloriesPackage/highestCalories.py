# Name: Aimee Madrigal
# email: ignaciac@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: March 28, 2024
# Course/Section: IS 4010 (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment uses a connection to SSMS to create a query and manipulate the pulled data in different ways.

# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this. This method takes all  the "rows"
# as a parameter, then pulls only the last two columns of the newly sorted top_5_calories list
# Citations: N/A
# Anything else that's relevant: N/A

# highestCalories.py

def getTop5(rows):
    '''
    takes rows as an argument and pulls the highest 5 calorie options
    @param rows from data
    @return list of 5 highest calorie items
    '''
    top_5_calories = rows[:5] # Acquires the first 5 rows
    return [(row[-2]) for row in top_5_calories] # This pulls only the product description column of top_5_calories list