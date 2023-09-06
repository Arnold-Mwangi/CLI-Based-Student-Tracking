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
from lib.models import Student, Subject, Base, session


if __name__ == '__main__':
    session.query(Student).delete()
    session.query(Subject).delete()

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


    subjects=[]
    for x in range (8):
        course_name, subject_code = random.choice(list(technical_courses.items()))
        subject=Subject(
            name= course_name,
            subject_code= subject_code
        )
        subjects.append(subject)
        session.add(subject)
    session.commit()
