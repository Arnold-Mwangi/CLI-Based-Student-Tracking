import os
import click
from .models import Subject, session, Student, Lesson

class SubjectManager:
    def __init__(self, session):
        self.session = session
        # self.reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")

    def add_subject(self, name, subject_code):
        new_subject = Subject(name=name, subject_code=subject_code)

        try:
            self.session.add(new_subject)
            self.session.commit()
            print(f"Subject '{name}' with code '{subject_code}' added successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error adding subject: {e}")



    def update_subject(self, subject_id):
            subject = self.session.query(Subject).filter_by(id=subject_id).first()

            if subject:
                print("Current Subject Details:")
                print(f"ID: {subject.id}")
                print(f"Name: {subject.name}")
                print(f"Code: {subject.subject_code}")

                new_name = input(f"Enter new name for subject '{subject.name}' (or press Enter to keep the current name): ")
                new_code = input(f"Enter new code for subject '{subject.subject_code}' (or press Enter to keep the current code): ")

                if new_name:
                    subject.name = new_name

                if new_code:
                    subject.subject_code = new_code

                print("\nUpdated Subject Details:")
                print(f"ID: {subject.id}")
                print(f"Name: {subject.name}")
                print(f"Code: {subject.subject_code}")

                confirmation = input("Confirm update (y/n): ").strip().lower()

                if confirmation == 'y':
                    try:
                        self.session.commit()
                        print(f"Subject '{subject.name}' with code '{subject.subject_code}' updated successfully.")
                    except Exception as e:
                        self.session.rollback()
                        print(f"Error updating subject: {e}")
                else:
                    print("Update canceled.")
            else:
                print(f"Subject with ID {subject_id} not found.")

    def get_subjects_by_student(self, student_id):
            # Query the lessons table to find subjects for the student
            subjects = (
                self.session.query(Subject)
                .join(Lesson, Lesson.subject_id == Subject.id)
                .filter(Lesson.student_id == student_id)
                .all()
            )

            if subjects:
                print(f"Subjects enrolled by Student ID {student_id}:")
                for subject in subjects:
                    print(f"Subject ID: {subject.id}, Name: {subject.name}, Code: {subject.subject_code}")
            else:
                print(f"Student with ID {student_id} is not enrolled in any subjects.")


    def get_subjects_by_teacher(self, teacher_id):
        teacher_id = input("Enter Teacher ID to retrieve subjects taught by the teacher: ").strip()

        # Check if the entered teacher_id is a valid integer
        try:
            teacher_id = int(teacher_id)
        except ValueError:
            print("Invalid Teacher ID. Please enter a valid integer ID.")
            return

        # Query the lessons table to find subjects taught by the teacher
        subjects = (
            self.session.query(Subject)
            .join(Lesson, Lesson.subject_id == Subject.id)
            .filter(Lesson.teacher_id == teacher_id)
            .all()
        )

        if subjects:
            print(f"Subjects taught by Teacher ID {teacher_id}:")
            for subject in subjects:
                print(f"Subject ID: {subject.id}, Name: {subject.name}, Code: {subject.subject_code}")
        else:
            print(f"Teacher with ID {teacher_id} is not teaching any subjects.")
subject_manager = SubjectManager(session)
