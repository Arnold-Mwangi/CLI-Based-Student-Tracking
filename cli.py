import click
from lib.model.students import student_manager

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

if __name__ == "__main__":
    cli()