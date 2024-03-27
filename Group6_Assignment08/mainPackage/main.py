# test.py
# Name: Connor Walsh
# email: walsh2ct@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 03/28/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment uses a connection string to SSMS to create a query and manipulate the pulled data in different ways

# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this. This is the main where we execute the query from, 
# and manipulate the resultant data set
# Citations: https://stackoverflow.com/questions/13207697/how-to-remove-square-brackets-from-list-in-python
# Anything else that's relevant: We each contributed to the modules that our respective documentation is in, but collaborated on the main here
import pyodbc
from connectPackage.connect import getTop5
from lowestCaloriesPackage.lowestCalories import getBottom5

#this is the connection string
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=GroceryStoreSimulator;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()

# For some reason SSMS wouldn't execute queries without this
cursor.execute('USE GroceryStoreSimulator;')

# Grab the data with our collaborated query
cursor.execute('SELECT DISTINCT tTransactionDetail.ProductID, tProduct.NameID, tName.Name, tProduct.Description, tProduct.Calories '
               'FROM tTransactionDetail '
               'INNER JOIN tProduct ON tTransactionDetail.ProductID = tProduct.ProductID '
               'INNER JOIN tName ON tProduct.NameID = tName.NameID '
               'ORDER BY tProduct.Calories DESC;')
rows = cursor.fetchall()
# Fetches all data and turns it into a list

#returns highest and lowest calorie items from rows as a list
highestCalorieList = getTop5(rows)
lowestCalorieList = getBottom5(rows)

#removes brackets and quotes from the lists to read as a grammatically correct sentence
print("These are the highest calorie items sold:",", ".join(highestCalorieList) + ".", "These are the lowest calorie items sold:", ", ".join(lowestCalorieList) + ".")