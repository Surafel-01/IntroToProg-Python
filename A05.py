# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using dictionaries and files to work with data
# Change Log: (Who, When, What)
#   Surafel Tebeje,05/24/2025,Created Script
# ------------------------------------------------------------------------------------------ #
# Define the Data Constants
import json

MENU:str='''\n---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
\n'''

FILE_NAME:str="Enrollments.json"

#Define the data variables
student_first_name:str=''
student_last_name:str=''
course_name:str=''
file:object=None
menu_choice:str
student_data:dict={}
students:list=[]


#Read a file data into a list of lists(table)
  #Extract data from file
try:
    file=open(FILE_NAME,'r')    #This is thinking that there is already a csv file created, otherwise, I got error message.
    students=json.load(file)
    file.close()
    print(students)
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

#Display MENU
while True:
    print(MENU)
    menu_choice=input("Enter your menu choice number: ")
#Process data and custom messages
    #Colelct user input data
    if menu_choice=="1":
     try:
       student_first_name=input("What is the student's first name? ")
       if not student_first_name.isalpha():
           raise ValueError("The first name should not contain numbers")
       student_last_name=input("What is the student's last name? ")
       if not student_last_name.isalpha():
           raise ValueError("The last name should not contain numbers")
       course_name=input("What is the course's name? ")
       student_data={"Student Name":student_first_name, "Student Last Name":student_last_name,"Course Name":course_name}
       students.append(student_data)
       print(f"\nstudent {student_first_name} {student_last_name} is registered!\n")
     except ValueError as e:
         print(e)
         print("-- Technical Error Message -- ")
         print(e.__doc__)
         print(e.str__())
     except Exception as e:
         print ("Error: There was a problem with your data!\n")
         print("---Technical Error Message--")
         print(e.__doc__)
         print(e.__str__())
         continue
     # Present the current data
    elif menu_choice == "2":
       for each in students:
           print(f"{each["Student Name"]},{each["Student Last Name"]},{each["Course Name"]}\n")
       continue
       # Save the data to a file
    elif menu_choice == "3":
       try:
           file = open(FILE_NAME, "w")
           json.dump(students,file)
           file.close()
           print("The following data is saved in the file:\n")
           print(students)
       except Exception as e:
           if file.closed== False:
              file.close()
           print("error: There was a problem in writing the file")
           print ("Please check that the file is not pen by another program")
           print("-- Technical Error Message -- ")
           print(e, e.__doc__)
           print(e.__str__())
       continue

    elif menu_choice=="4":
           print("program Ended!")
        #Stop the loop
           break
    else:
           print("Invalid menu choice")





