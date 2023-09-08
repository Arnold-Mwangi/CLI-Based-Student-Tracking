import os
import click
from .models import Subject, session, Student, Lesson, Teacher
from tabulate import tabulate

class TeacherManager:
    def __init__(self, session):
        self.session = session

    def create_teacher(self, name, phone, subject_id):
        teacher = Teacher(name=name, phone=phone, subject_id=subject_id)

        try:
            self.session.add(teacher)
            self.session.commit()
            print(f"Teacher '{name}' with Phone '{phone}' assigned to Subject ID '{subject_id}' created successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error creating teacher: {e}")

    def generate_teacher_report(self, teacher_id):
            teacher = self.session.query(Teacher).filter_by(teacher_id=teacher_id).first()

            if teacher:
                subjects_taught = []
                students_taught = []

                # Fetch subjects and students from lessons table
                lessons = self.session.query(Lesson).filter_by(teacher_id=teacher_id).all()

                for lesson in lessons:
                    subjects_taught.append(lesson.subject.name)
                    students_taught.append(lesson.student.name)

                print(f"Teacher Name: {teacher.name}")
                print("Subjects Taught:")
                print(tabulate(subjects_taught, headers=["Subject"], tablefmt="grid"))
                print("Students Taught:")
                print(tabulate(students_taught, headers=["Student"], tablefmt="grid"))
            else:
                print(f"Teacher with ID {teacher_id} not found.")

teacher_manager = TeacherManager(session)