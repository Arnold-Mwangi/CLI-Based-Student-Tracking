import sys
import os
from datetime import datetime
from .models import Student, session

# Add the parent directory (project directory) to the Python path
current_dir = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_dir)

class StudentManager:
    def __init__(self, session):
        self.session = session

    def create_student(self, first_name, last_name, gender, phone_number):
        student = Student(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            phone_number=phone_number
        )

        self.session.add(student)
        self.session.commit()

        return student

    def addstudent(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        gender = input("Enter gender: ")
        phone_number = input("Enter phone number: ")

        current_year = datetime.now().year
        last_two_digits_of_year = current_year % 100

        admission_id_prefix = f"BUK/{last_two_digits_of_year}/"

        student = Student(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            phone_number=phone_number,
            admission_id = None
        )

        self.session.add(student)
        self.session.commit()
        
        new_student_id = student.student_id

        admission_id =f"{admission_id_prefix}{new_student_id}"

        student.admission_id =admission_id
        
        self.session.add(student)

        self.session.commit()

        print(f"Student {student.first_name} added to bukara with admission ID: {admission_id}")

        return student

student_manager = StudentManager(session)


new_student = student_manager.addstudent()