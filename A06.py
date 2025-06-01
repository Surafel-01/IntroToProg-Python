# ------------------------------------------------- #
# Title: A06 - Working with Functions, Classes and SoC
# Description: Demonstrates how to use Functions, classes and the SoC pattern
# ChangeLog: (Who, When, What)
# Surafel Tebeje,05.30.2025,Created Script
# ------------------------------------------------- #

import json

# Define the Data Constants
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
menu_choice:str=''
students:list=[]

# Processing --------------------------------------- #
class FileProcessor:
    """ A collection of processing layer functions that work with Json files
        ChangeLog: (Who, When, What)
        Surafel Tebeje,05.30.2025,Created Class
       """

    @staticmethod
    def read_data_from_file(file_name:str, student_data:list):
        """This function reads data from a json file and loads into a list of dictionary rows
        ChangeLog: (Who, When, What)
        Surafel Tebeje,05.30.2025, created function
        parameter: file_name :string data with name of file to read from
        parameter: student_data: list of dictionary rows with multiple student registrations
        return: returns the list of dictionary rows
        """
        file=None  #a local variable
        try:
           file= open(file_name, "r")
           student_data = json.load(file)
           file.close()
        except FileNotFoundError as e:
           IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
           IO.output_error_messages("There was a non-specific error!", e)
        finally:
           if file.closed == False:
              file.close()
        return student_data

    @staticmethod
    def write_data_to_file (file_name:str, student_data:list):
        """This function writes data to a json file
        ChangeLog: (Who, When, What)
        Surafel Tebeje,05.30.2025, created function"""
        file=None
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format",e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        print("The following data is saved in the file:\n")
        print(students)
class IO:
    """
        A collection of presentation layer functions that manage user input and output
        ChangeLog: (Who, When, What)
        Surafel Tebeje,05.30.2025,Created Class
        Surafel Tebeje,05.30.2025,Added menu output and input functions
        Surafel Tebeje,05.30.2025,Added a function to display the data
        Surafel Tebeje,05.30.2025,Added a function to display custom error messages
        """

    @staticmethod
    def output_error_messages (message:str, error:Exception=None):
        """ This function displays a custom error messages to the user

                ChangeLog: (Who, When, What)
                Surafel Tebeje,05.30.2025,Created function
                :return: None
                """
        message="There is a problem with your data. Please try to find out!"
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu (menu:str):
        """ This function displays the menu of choices to the user

                ChangeLog: (Who, When, What)
                Surafel Tebeje,05.30.2025,Created function"""
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user
                :return: string with the users choice
                """

        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
               raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message
        return choice


    @staticmethod
    def input_student_data(student_data:list):
        """This function gets a student data from a user, and returns data.
        The function stores data into a list (students) which will be returned at the end.
            ChangeLog: (Who, When, What)
            Surafel Tebeje,05.30.2025,Created function"""

        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers")
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers")
            course_name = input("What is the course's name? ")
            student_data = {"Student Name": student_first_name, "Student Last Name": student_last_name,
                            "Course Name": course_name}
            students.append(student_data)
            print(f"\nstudent {student_first_name} {student_last_name} is registered!\n")
        except ValueError as e:
            IO.output_error_messages ("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


    @staticmethod
    def output_student_courses(student_data: list):
        """This function displays the registered student data
        ChangeLog: (Who, When, What)
            Surafel Tebeje,05.30.2025,Created function"""

        for each in student_data:
            print(f"{each['Student Name']},{each['Student Last Name']},{each['Course Name']}\n")


#  End of function definitions

# Beginning of the main body of this script

#Read contents of a file
students=FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks

while True:

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Register the student for a course
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":  # Show the current data
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
       FileProcessor.write_data_to_file(file_name= FILE_NAME, student_data=students)
       continue

    elif menu_choice == "4":  # End the program
        print("program Ended!")
        break  # out of the while loop
    else:
        print("Invalid menu choice")