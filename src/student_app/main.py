from student_app.logger import logger
from utils.validation import validate_marks
from services.calculator import calculate_grade

def main():
    logger.info("Application started.")
    print("--- Student Grade Calculator ---")
    
    user_input = input("Enter student marks (0-100): ")
    
    try:
        # Validation
        clean_marks = validate_marks(user_input)
        
        # Calculation
        grade = calculate_grade(clean_marks)
        
        # Output Results
        print(f"\n[Result]: Marks = {clean_marks} | Final Grade = {grade}")
        logger.info("Application execution completed successfully.")
        
    except ValueError as e:
        logger.error(f"Application error caught: {e}")
        print(f"\n[Error]: {e}")
    except Exception as e:
        logger.critical(f"Unexpected critical error: {e}")
        print(f"\n[Critical Error]: An unexpected error occurred.")

if __name__ == "__main__":
    main()


''''
STAGE 03

def validate_name(name):
    return name != ""

def validate_marks(marks):
    return 0 <= marks <= 100

def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70: 
        return "B"
    elif marks >= 60: 
        return "C" 
    elif marks >= 50: 
        return "D" 
    else: 
        return "F"

def main():
    name = input("Enter student name: ") 
    
    if not validate_name(name):
        print("Invalid name") 
        return 
    
    marks = int(input("Enter marks: ")) 
    
    if not validate_marks(marks): 
        print("Invalid marks") 
        return 
    grade = calculate_grade(marks) 
    print("\nStudent Report") 
    print("----------------") 
    print(f"Name: {name}") 
    print(f"Marks: {marks}") 
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()

'''





















































'''
STAGE 02

def main():
    name = input("Enter student name: ") 
    if name == "": 
        print("Invalid name") 
        return  
    
    marks = int(input("Enter marks: ")) 
    if marks < 0 or marks > 100:
        print("Invalid marks") 
        return 
    if marks >= 80:
        grade = "A" 
    elif marks >= 70:
        grade = "B" 
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D" 
    else: 
        grade = "F" 
    
    print("\nStudent Report") 
    print("----------------") 
    print(f"Name: {name}") 
    print(f"Marks: {marks}") 
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()

'''



