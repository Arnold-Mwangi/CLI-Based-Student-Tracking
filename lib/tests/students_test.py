from lib.models.models import Student
from class_methods.students import createstudent

new_student = createstudent('Arnold', 'Kirigwi', 'Male', '0746633768')
print(new_student)