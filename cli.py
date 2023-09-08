import click
from lib.model.students import student_manager as student_manager
from lib.model.subjects import subject_manager
from lib.model.teachers import teacher_manager
from lib.model.teachers import TeacherManager


@click.group()
def cli():
    pass

@cli.group()
def students():
    pass


@students.command()
def add():
    # student_manager = StudentManager(session)
    student_manager.addstudent()

@cli.group()
def subjects():
    pass

@subjects.command()
@click.option('--name', prompt='Enter subject name', help='Name of the subject')
@click.option('--subject_code', prompt='Enter subject code', help='Code of the subject')
def add(name, subject_code):
    subject_manager.add_subject(name, subject_code)

@subjects.command()
@click.option('--subject_id', prompt='Enter subject ID to update', help='ID of the subject to update')
def update(subject_id):
    subject_manager.update_subject(subject_id)

@subjects.command(name='getsubjectbystudent')  # Renamed command to 'getsubjectbystudent'
@click.option('--student_id', prompt='Enter student ID to retrieve enrolled subjects', help='ID of the student')
def get_subjects_by_student(student_id):
    # subject_manager = SubjectManager(session)
    subject_manager.get_subjects_by_student(student_id)

@subjects.command()
@click.option('--teacher_id', prompt='Enter teacher ID to retrieve subjects taught by the teacher', help='ID of the teacher')
def getsubjectbyteacher(teacher_id):
    subject_manager.get_subjects_by_teacher(teacher_id)

@cli.group()
def teachers():
    pass

@teachers.command()
@click.option('--name', prompt='Enter teacher name', help='Name of the teacher')
@click.option('--phone', prompt='Enter teacher phone', help='Phone number of the teacher')
@click.option('--subject_id', prompt='Enter subject ID', help='ID of the subject')
def create(name, phone, subject_id):
    teacher_manager.create_teacher(name, phone, subject_id)  # Use teacher_manager to create a teacher

@teachers.command(name='generate-report')  # Change the command name here
@click.option('--teacher_id', prompt='Enter teacher ID', help='ID of the teacher')
def generate_report(teacher_id):
    # teacher_manager = TeacherManager(session)
    teacher_manager.generate_teacher_report(teacher_id)

if __name__ == "__main__":
    cli()