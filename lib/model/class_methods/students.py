import sys
import os
from ..models import Student, session

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



student_manager = StudentManager(session)

# Usage example
new_student = student_manager.create_student('Arnold', 'Kirigwi', 'Male', '0746633768')
print(new_student)
