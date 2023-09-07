from sqlalchemy import String, Integer, PrimaryKeyConstraint,CheckConstraint, Boolean, ForeignKeyConstraint, ForeignKey, MetaData, Sequence,Column, text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, UniqueConstraint, Table
from datetime import datetime
import os

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention= convention)

Base = declarative_base(metadata=metadata)

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

db_file = os.path.join(project_dir, 'model', 'bukura.db')
engine = create_engine(f'sqlite:///{db_file}')


Session = sessionmaker(bind =  engine)

session = Session()

student_subject_association = Table(
    'student_subject_association',
    Base.metadata,
    Column('student_id', Integer(), ForeignKey('students.student_id')),
    Column('subject_id', Integer, ForeignKey('subjects.id'))
)

class Student(Base):
    __tablename__ = "students"


    student_id = Column(Integer(), primary_key =True, autoincrement=True)
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    phone_number = Column(String())
    admission_id = Column(String(), nullable=True)

    teachers = relationship('Teacher', back_populates='student')
    subjects = relationship('Subject', secondary=student_subject_association, back_populates='students')
    attendances = relationship("Attendance", back_populates="student")
    grades = relationship('Grade', back_populates='student')
        

    def __repr__(self):
        return f"<Student {self.first_name}  {self.gender}  {self.phone_number}"

class Subject(Base):
    __tablename__ = "subjects"
    __table_args__ = (UniqueConstraint('subject_code', name='uq_subject_code'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String())
    subject_code = Column(String())

    teachers = relationship('Teacher', back_populates='subject')
    attendances = relationship('Attendance', back_populates='subject') 
    students =relationship('Student', secondary=student_subject_association, back_populates='subjects')

    grades = relationship('Grade', back_populates='subject') 


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject_id = Column(String, ForeignKey('subjects.id'))

    student = relationship('Student', back_populates='teachers')
    subject=relationship('Subject', back_populates='teachers')


class Attendance(Base):
    __tablename__ = 'attendances'


    attendance_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    attendance_date = Column(DateTime, default=datetime.now)
    checkin_time = Column(DateTime)
    checkout_time = Column(DateTime)
    attendance_status = Column(Boolean()) 
    
    student = relationship("Student", back_populates="attendances")
    subject = relationship("Subject", back_populates="attendances")


class Grade(Base):
    __tablename__ = 'grades'

    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade_value = Column(Integer())

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")