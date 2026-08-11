def greet(name):
    print("Hello", name)
    print("Welcome to the Student Utility App!")

def calculator():
    try:
        expression = input("Enter calculation: ")
        result = eval(expression)
        print("Result:", result)

    except:
        print("Invalid calculation!")


def age_checker():
    try :
        age = int(input("Enter your age: "))

        if age <= 12:
            print("You are a child.")
        elif age <= 17:
            print("You are a teenager.")
        else:
            print("You are an adult.")
    except :
        print ("Please Enter a valid age!")

def student_details():
    name = input("Enter your name: ")
    grade = input("Enter your grade: ")
    school = input("Enter your school: ")

    if not name:
        print("Name cannot be empty!")

    elif not grade:
        print("Grade cannot be empty!")

    elif not school:
        print("School cannot be empty!")

    else :
        print("\n--- Student Details ---")
        student = {"name": name,"grade": grade,"school": school}
        print("Name:", student["name"])
        print("Grade:", student["grade"])
        print("School:", student["school"])

def number_checker():
    try :
        integer = int(input("Enter a number: "))

        if integer > 0:
            if integer % 2 == 0:
                print("Positive")
                print("Even")
            else:
                print("Positive")
                print("Odd")
        elif integer < 0:
            if integer % 2 == 0:
                print("Negative")
                print("Even")
            else:
                print("Negative")
                print("Odd")
        else:
            print("Zero")
            print("Even")

    except :
        print ("Please Enter a valid number!")


greet("Harsh")

while True:
    print("\n========================")
    print("   STUDENT UTILITY APP")
    print("========================")
    print("1. Calculator")
    print("2. Age Checker")
    print("3. Student Details")
    print("4. Number Checker")
    print("5. Exit")

    choice = input("\nChoose an option number: ")

    # This part is for the Calculator
    if choice == "1":
        calculator()

    # This part is for the Age Checker
    elif choice == "2":
        age_checker()

    # This part is for the Student Details
    elif choice == "3":
        student_details()

    # This part is for the Number Checker
    elif choice == "4":
        number_checker()

    # This part is for the Exit
    elif choice == "5":
        print("Thanks for using the Student Utility App!")
        break

    else:
        print("Invalid choice. Please try again.")
