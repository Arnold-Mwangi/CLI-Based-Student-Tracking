import os
import sys
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker

# Get the directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Append the project's root directory to the Python path
sys.path.append(project_root)

# Now you can import modules from the 'lib' package (not 'db')
from lib.models import Student, Subject, Base, session, Teacher


if __name__ == '__main__':
    session.query(Student).delete()
    session.query(Subject).delete()
    session.query(Teacher).delete()
    


    fake = Faker()

    def clean_phone_number(phone_number):
        cleaned_number = ''.join(filter(str.isdigit, phone_number))
        return cleaned_number

    students = []
    for x in range(50):
        student = Student(
            first_name=fake.unique.first_name(),
            last_name=fake.unique.last_name(),
            gender=fake.random_element(elements=('Male', 'Female')),
            phone_number=clean_phone_number(fake.unique.phone_number())
        )

        session.add(student)
        students.append(student)
    
    session.commit()

    technical_courses = {
        "Machine Learning and Artificial Intelligence": "CS101",
        "Data Science": "DS202",
        "Web Development": "WD303",
        "Cybersecurity": "CS404",
        "Cloud Computing": "CC505",
        "Mobile App Development": "MAD606",
        "Blockchain Technology": "BT707",
        "Big Data and Hadoop": "BDH808"
    }

    subjects = []
    used_subject_codes = set()

    for _ in range(8):
        available_courses = [course for course in technical_courses.items() if course[1] not in used_subject_codes]
        if not available_courses:
            break  # No more unique subject codes available
        course_name, subject_code = random.choice(available_courses)
        used_subject_codes.add(subject_code)
        
        subject = Subject(
            name=course_name,
            subject_code=subject_code
        )
        subjects.append(subject)
        session.add(subject)

    session.commit()

teacher_names = ["Alice Smith", "John Johnson", "Emily Davis", "Michael Wilson"]

teachers = []
# Create a shuffled list of student IDs
shuffled_student_ids = [student.student_id for student in students]
random.shuffle(shuffled_student_ids)

# Create a list of associations
associations = []

# Create instances of Teacher with shuffled student IDs and random subjects
for teacher_name in teacher_names:
    for x in range(len(students)):
        if not shuffled_student_ids:  # If the list is empty, shuffle it again
            shuffled_student_ids = [student.student_id for student in students]
            random.shuffle(shuffled_student_ids)
        
        # Pop a student ID from the shuffled list
        student_id = shuffled_student_ids.pop()

        # Randomly select a subject from the existing records
        subject = random.choice(subjects)
        
        teacher = Teacher(
            name=random.choice(teacher_names), 
            student_id=student_id, 
            subject_id=subject.id)
            
        session.add(teacher)
        associations.append((teacher, student_id, subject))

# Commit the session to save the teachers to the database
try:
    session.commit()
    print("Teachers seeded successfully.")
    for teacher, student_id, subject in associations:
        print(f"Teacher: {teacher.name}, Student ID: {student_id}, Subject: {subject.name}")
except Exception as e:
    session.rollback()
    print(f"Error during session commit: {str(e)}")




