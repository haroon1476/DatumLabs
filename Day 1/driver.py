# Testing variables
# name = "Haroon Ur Rasheed"
# age = 22
# univeristyName = "PUCIT Lahore"
# print("name is " + name + " , age is " + str(age) + " and univerisity name is " + univeristyName)

# name = input("Please enter your name : ")
# print("The entered name is " + name)

# Testing type conversions
# age = input("Please enter your age")
# age = int(age)
# print("your age is " + str(age))
# print(type(age))


# Testing loops
# For Loops
# for var in range(5):
#   print(var)

fruits = ["apples" , "mangoes" , "guavas" , "bananas"]
for index,fruit in enumerate(fruits):
  print(f"The Current fruit with index {index} is {fruit}")  


#While loops
# count = 0
# while(count < 10):
#     print(f"The current count is {count}")
#     count = count +1

 # Testing control statements
# for var in range(10):
#     if(var == 5):
#         continue
#     if(var == 8):
#         break
#     print(f"The current value of count is {var}")


# Testing functions in python
# def greetings():
#     print("Welcome to Datum Labs Haroon Ur Rasheed!")
#     return

# def printAge(name , age):
#     print(f"The age of {name} is {age}")


def getProduct(a , b) :
    return a*b  


# #func call
# # greetings()
# # printAge("haroon" , 22)

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# print(f"The product of {a} and {b} is {getProduct(a,b)}")

#local variables inside the fuctions
# def myFunc():
#     x = 10
#     print(x)



# # testing arbitrary parameters
# def printNumber(*args):
#     for index,number in enumerate(args):
#         print(f"Number at index {index} is {number}") 


# printNumber(2,2,3,4,5,5,6,6,4)       


# testing classes in python
# class Person:

#     # Adding static members in the class
#     scientificName = "Homo Sapiens"

#     # constructor of person class
#     def __init__(self , name , age , univeristy):
#         self.name = name
#         self.age = age
#         self.universityName = univeristy

#     def printStudentInformation(self):
#         print(f"Name = {self.name} , Age = {self.age} , University Name = {self.universityName}")


# #Creating an object of the person class
# Person1 = Person("Haroon Ur Rasheed" , 22 , "PUCIT Lahore")
# Person1.printStudentInformation()
# print(Person1.scientificName)


# days = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]
# print(days[1:-2])
# print("Thursday" in days)

# # Adding at the end of the list
# days.append("NoDay")
# print(days)

# # Adding at a specific location in the list
# days.insert(3, "AtSomeIndex")
# print(days)


# #Use of extend function
# animals = ["Cow" , "Lion"]
# animals.extend(["Tiger" , "Snake"])
# print(animals)


# numbers = [2,4,12,4,23,32,12]
# sortedNumbers = sorted(numbers)
# print(sortedNumbers)

# # Testing list comprehensions here
# squaredNumbers = [x*x for x in sortedNumbers]
# print("Squared Numbers are ")
# print(squaredNumbers)


# multitypeItems = ["Haroon" , 21 , 2.343 , "PUCIT"]
# print(multitypeItems)


# # Simple dictionaries in python
# Student = {
#     "name" : "Haroon Ur Rasheed",
#     "age" : 21 ,
#     "university" : "PUCIT",
#     "company" : "Datum Labs"
# }

# print(Student)
# print(Student["company"])

# #Modifying the dictionat
# Student["age"] = 22
# print(Student)

# #Adding new key value pair
# Student["City"] = "Lahore"
# print(Student)

# # deleting a key value pair
# del Student["university"]
# print(Student)

# # company = Student["company"]
# # print(company)

# print(Student.keys())
# print(Student.values())
# print(Student.items())

# tiger = {
#     "name" : "tiger",
#     "age" : 32,
#     "nickName" : "prince"
# }

# lion = {
#     "name" : "lion",
#     "age" : 42,
#     "nickName" : "king"
# }

# tiger.update(lion)
# print(lion)
# print(tiger)


# Nested Dictionary
# student = {
#     "name": "Alice",
#     "info" : {
#         "age" : 21,
#         "major" : "Computer Science"
#     }

#     # "info": {
#     #     "age": 21,
#     #     "major": "Computer Science"
#     # }
# }


# print(student["info"]["major"])
#print(student["info"]["age"])  # Output: 21

#Dictionary comprehnsions
# squaredNumbers = {x:x*2 for x in range(10)}
# print(squaredNumbers)


#Working with JSONS in python

# import json
# Student = {
#     "name" : "Haroon Ur Rasheed" ,
#     "male" : True,
#     "age" : 22
# }

# jsonedStudent = json.dumps(Student)
# print(Student)
# print(jsonedStudent)
# originalStudent = json.loads(jsonedStudent)
# print(originalStudent)


# import json

# # Reading Data from  a JSON FIle
# with open('data.json' , 'r') as file:
#     data = json.load(file)


# print(data)


# # Writing data to a JSON File
# Nationality = {
#     "Country" : "Pakistan",
#     "City" : "Lahore"
# }

# with open('data.json' , 'w') as file:
#     json.dump(Nationality, file)


# import json

# # Manipulating the JSON Data
# with open('data.json' , 'r') as file:
#     information = json.load(file)

# print(information)   
# information['Country'] = "India"
# information["Continent"] = "Asia"

# with open('data.json' , 'w') as file:
#     json.dump(information, file)


# print("Updated information added successfully!")


# import csv

# # Reading data from a csv file
# with open('data.csv' , 'r') as file:
#     csv_reader = csv.reader(file)

#     for row in csv_reader:
#         print(row)


# # Another way to read data
# with open('data.csv' , 'r') as file:
#     csv_reader = csv.DictReader(file)

#     for row in csv_reader:
#         print(row)


# import csv

# Writing to a CSV file
# data = [
#     ['name', 'age', 'city'],
#     ['Usman Asif', 22, 'Lahore'],
#     ['Abdullah Hamid', 30, 'Karachi'],
   
# ]

# with open('output.csv', 'w') as file:

#     # creating an object for writing
#     csv_writer = csv.writer(file)
    
#     # Writing rows to the CSV file
#     csv_writer.writerows(data)


# import csv
# #updating haroon's information using csv

# # Generic function to read a file using its filename as a function parameter
# def readFile(filename):
#     with open(filename , 'r') as file:
#       csv_reader = csv.reader(file)
#       rows = list(csv_reader) # All rows attained
#       return rows


# rows = readFile('data.csv') # function call
# for row in rows:
#     if row[0] == 'Haroon':  # Checking if name is Haroon
#         row[1] = '22'  # Update the age to 31


# def writeDataToFile(filename , data):
#     # Writing the updated data back to the CSV file
#     with open(filename, mode='w') as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerows(data)  # Writing all rows back to the file

# #function call to write data back to file
# writeDataToFile('data.csv' , rows)
# print("Haroon's age updated successfully.")