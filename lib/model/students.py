import sys
import os
from datetime import datetime
from .models import Student, session
from tabulate import tabulate
import click

# Add the parent directory (project directory) to the Python path
current_dir = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_dir)

class StudentManager:
    def __init__(self, session):
        self.session = session
        self.reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")



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


    def update_student(self):
        student_id =input("Enter the Student ID you want to update:")
        student = session.query(Student).filter_by(student_id = student_id).first()
        if student:
            print("Current Student Details:")
            print(f"Student ID: {student.student_id}")
            print(f"First Name: {student.first_name}")
            print(f"Last Name: {student.last_name}")
            print(f"Gender: {student.gender}")
            print(f"Phone Number: {student.phone_number}")
            print(f"Phone Number: {student.admission_id}")

            new_info = {}
            fields = ["first_name", "last_name", "gender", "phone_number"]

            for field in fields:
                value = input(f"Enter new {field} (or press enter to keep current value)")

                if value:
                    new_info[field] = value

            if new_info:
                print("\n Updated Student Details:")
                for key, value in new_info.items():
                    print(f"{key} : {value}")

                confirmation = input("Confirm update (y/n): ".strip().lower())
                
                if confirmation == 'y':
                    for key, value in new_info.items():
                        setattr(student, key, value)

                    session.commit()
                    print("Student details updated successfully.")
                else:
                    print("Updated Canceled.")
            else:
                print("No changes Made")
        else:
            print(f"Student with Id of: {student_id} not found")



    def get_student_by_id(self):
        student_id = input("Enter student's Id to get to view admission number").strip().lower()
        try:
            student_id = int(student_id)
        except ValueError:
            print("Error: Invalid ID. Please enter a valid integer ID.")
            return

        student = session.query(Student).filter_by(student_id = student_id).first()
        if student:
            print(f"\nPhone Number: {student.admission_id}")
            print("Other Student Details:")
            print(f"Student ID: {student.student_id}")
            print(f"First Name: {student.first_name}")
            print(f"Last Name: {student.last_name}")
            print(f"Gender: {student.gender}")
            print(f"Phone Number: {student.phone_number}")
            
        else:
            print(f"Error: Student with ID {id} does not exist.")
    

    def delete_student(self):
        student_id = input("Enter student's Id to get to view admission number::   ").strip().lower()
        try:
            student_id = int(student_id)
        except ValueError:
            print("Error: Invalid ID. Please enter a valid integer ID.")
            return

        student = session.query(Student).filter_by(student_id = student_id).first()
        if student:
            confirmation = input(f"Confirm deletion of {student_id} ::{student.first_name} (y/n)::   ").strip().lower()
            if confirmation == 'y':
                session.delete(student)
                session.commit()
                print(f"Successfully deleted {student.first_name}")
            else:
                print(f"Deletion of {student.first_name} canceled")
        else:
            print(f"Error: Student with ID {student_id} does not exist.")


    def generate_student_report(self):
        student_id = input("Enter student id to generate his/her report::   ").strip().lower()

        try:
            student_id = int(student_id)
        except ValueError:
            print("Enter a valid ID ")
            student_id = input("Enter student id to generate his/her report::   ")

        student = self.session.query(Student).filter_by(student_id=student_id).first()

        if not student:
            print(f"Student with ID {student_id} does not exist.")
            return

        table_data =[]

        table_data.append(["Subject", "Grade", "Attendance Date", "Check-in Time", "Checkout Time"])

        for grade in student.grades:
            subject = grade.subject
            attendance_records = [attendance for attendance in subject.attendances if attendance.student_id == student_id]

            for attendance in attendance_records:
                table_data.append([
                    subject.name,
                    grade.grade_value,
                    attendance.attendance_date,
                    attendance.checkin_time,
                    attendance.checkout_time
                ])
        print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

        student_folder_name = f"{student.first_name}_{student.admission_id}"
        student_folder_path = os.path.join(self.reports_dir, student_folder_name)
        os.makedirs(student_folder_path, exist_ok=True)

        report_file_name = f"{datetime.now()}::report.txt"
        report_file_path = os.path.join(student_folder_path, report_file_name)

        with open(report_file_path, "w") as report_file:
            report_file.write(tabulate(table_data, headers="firstrow", tablefmt="grid"))

        print(f"Report saved as {report_file_path}")


student_manager = StudentManager(session)
# # new_student = student_manager.addstudent()

# # student_manager.update_student()
# # student_manager.get_student_by_id()
# # student_manager.delete_student()
# student_manager.generate_student_report()