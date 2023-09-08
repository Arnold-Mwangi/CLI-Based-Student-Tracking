import os
import sys
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from faker import Faker

# Get the directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Append the project's root directory to the Python path
sys.path.append(project_root)

# Now you can import modules from the 'lib' package (not 'db')
from models import Student, Subject, Base, session, Teacher, Attendance, Grade, Lesson


if __name__ == '__main__':
    session.query(Student).delete()
    session.query(Subject).delete()
    session.query(Teacher).delete()
    session.query(Attendance).delete()
    session.query(Grade).delete()
    


    fake = Faker()

    def clean_phone_number(phone_number):
        cleaned_number = ''.join(filter(str.isdigit, phone_number))
        return cleaned_number

    students = []
    current_year = datetime.now().year
    last_two_digits_of_year = current_year % 100

    admission_id_prefix = f"BUK/{last_two_digits_of_year}/"

    for x in range(50):
        student = Student(
            first_name=fake.unique.first_name(),
            last_name=fake.unique.last_name(),
            gender=fake.random_element(elements=('Male', 'Female')),
            phone_number=clean_phone_number(fake.unique.phone_number()),
            admission_id = None
        )

        session.add(student)
        students.append(student)
    
        session.commit()

        new_student_id = student.student_id

        admission_id =f"{admission_id_prefix}{new_student_id}"

        student.admission_id =admission_id
            
        session.add(student)

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

    # ...

#     teacher_names = ["Alice Smith", "John Johnson", "Emily Davis", "Michael Wilson"]

#     # Create a list of unique subject IDs
#     unique_subject_ids = [subject.id for subject in subjects]

#     teachers = []

#     # Create instances of Teacher with shuffled student IDs and random subjects
#     for student in students:
#         # Shuffle the list of unique subject IDs to ensure randomness
#         random.shuffle(unique_subject_ids)

#         # Take the first 4 subjects from the shuffled list (or fewer if there are fewer unique subjects)
#         assigned_subjects = unique_subject_ids[:4]

#         for teacher_name, subject_id in zip(teacher_names, assigned_subjects):
#             teacher = Teacher(
#                 name=teacher_name,
#                 student_id=student.student_id,
#                 subject_id=subject_id
#             )
#             session.add(teacher)
#             teachers.append((teacher, student.student_id, subject_id))

#     # Commit the session to save the teachers to the database
#     try:
#         session.commit()
#         print("Teachers seeded successfully.")
#         for teacher, student_id, subject_id in teachers:
#             print(f"Teacher: {teacher.name}, Student ID: {student_id}, Subject: {subject_id}")
#     except Exception as e:
#         session.rollback()
#         print(f"Error during session commit: {str(e)}")

#     # ...

#     attendances = []
#     for teacher, student_id, subject_id in teachers:
#         attendance_record = Attendance(
#             student_id=student_id,
#             subject_id=subject_id,
#             attendance_date=datetime.now(),
#             checkin_time=datetime.now(),
#             checkout_time=None,
#             attendance_status=False
#         )

#         session.add(attendance_record)
#         attendances.append(attendance_record)

#     session.commit()



    
# # Create a dictionary to map students to their subjects
# student_subject_mapping = {}
# for teacher, student_id, subject_id in teachers:
#     if student_id not in student_subject_mapping:
#         student_subject_mapping[student_id] = []
#     student_subject_mapping[student_id].append(subject_id)


# grades = []

# # Iterate through students and assign grades for the subjects they are teaching
# for student in students:
#     student_id = student.student_id

#     # Check if the student is teaching any subjects
#     if student_id in student_subject_mapping:
#         subject_ids = student_subject_mapping[student_id]
        
#         for subject_id in subject_ids:
#             grade_value = random.randint(0, 100)

#             grade = Grade(
#                 student_id=student_id,
#                 subject_id=subject_id,
#                 grade_value=grade_value
#             )

#             session.add(grade)
#             grades.append(grade)

#             print(f"Assigned Grade: Student ID {student_id}, Subject ID {subject_id}, Grade {grade_value}")

# # Commit the session to save the grades to the database
# try:
#     session.commit()
#     print("Grades seeded successfully.")
# except Exception as e:
#     session.rollback()
#     print(f"Error during session commit: {str(e)}")


    num_teachers = 10  # Total number of teachers to create
    max_teachers_per_subject = 3  # Maximum number of teachers per subject

    # Assuming you have subjects defined in your database
    subjects = session.query(Subject).all()

    teachers = []

    # Create a list of subjects to keep track of assigned subjects
    assigned_subjects = []

    # Distribute teachers among subjects
    while num_teachers > 0:
        for subject in subjects:
            if num_teachers == 0:
                break

            # Check if the subject already has the maximum number of teachers
            if subject.id not in assigned_subjects or len(subject.teachers) < max_teachers_per_subject:
                teacher_name = fake.name()
                phone_number = "254" + "".join([str(random.randint(0, 9)) for _ in range(9)])
                
                teacher = Teacher(name=teacher_name, phone=phone_number, subject_id=subject.id)
                teachers.append(teacher)

                assigned_subjects.append(subject.id)
                num_teachers -= 1

    # Add and commit the teachers to the database
    session.add_all(teachers)
    session.commit()

    # Close the session
    session.close()

    # Retrieve students, subjects, and teachers from the database
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    teachers = session.query(Teacher).all()

    # Define the maximum number of subjects per student
    max_subjects_per_student = 3

    # Create a list to store the generated lessons
    lessons = []


# Create a list to store the generated lessons
lessons = []

# Create a dictionary to track the number of subjects assigned to each student
subjects_assigned_count = {}

# Seed lessons for each student
for student in students:
    # Shuffle the subjects to randomize their order
    random.shuffle(subjects)

    # Initialize the count for the current student
    subjects_assigned_count[student.student_id] = 0

    for subject in subjects:
        # Check if the student has reached the maximum number of subjects
        if subjects_assigned_count[student.student_id] >= max_subjects_per_student:
            break

        # Check if the student is already assigned to the current subject
        if not any(lesson.student_id == student.student_id and lesson.subject_id == subject.id for lesson in lessons):
            # Find a teacher who teaches the current subject
            teacher = next((t for t in teachers if t.subject_id == subject.id), None)

            # If a teacher is found, create a lesson for the student
            if teacher:
                lesson = Lesson(
                    teacher_id=teacher.teacher_id,
                    subject_name=subject.name,
                    student_id=student.student_id,
                    subject_id=subject.id
                )
                lessons.append(lesson)
                subjects_assigned_count[student.student_id] += 1

                # Check if we have reached the desired total number of lessons (150)
                if len(lessons) == 150:
                    break

# Add and commit the generated lessons to the database
session.add_all(lessons)
session.commit()

# Close the session
session.close()


lessons = session.query(Lesson).all()

attendances = []
for lesson in lessons:
    # Create an attendance record for the lesson
    attendance_record = Attendance(
        student_id=lesson.student_id,
        subject_id=lesson.subject_id,
        attendance_date=datetime.now(),
        checkin_time=datetime.now(),
        checkout_time=None,
        attendance_status=False
    )

    session.add(attendance_record)
    attendances.append(attendance_record)

    # Limit the total number of attendance records to a maximum of 150
    if len(attendances) >= 150:
        break

session.commit()

