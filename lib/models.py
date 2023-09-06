from sqlalchemy import String, Integer, PrimaryKeyConstraint,CheckConstraint, Boolean, ForeignKeyConstraint, ForeignKey, MetaData, Sequence,Column, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, UniqueConstraint, Table

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention= convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///bukura.db')

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

    teachers = relationship('Teacher', back_populates='student')
    subjects = relationship('Subject', secondary=student_subject_association, back_populates='students')


class Subject(Base):
    __tablename__ = "subjects"
    __table_args__ = (UniqueConstraint('subject_code', name='uq_subject_code'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String())
    subject_code = Column(String())

    teachers = relationship('Teacher', back_populates='subject')
    students =relationship('Student', secondary=student_subject_association, back_populates='subjects')


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject_id = Column(String, ForeignKey('subjects.id'))

    student = relationship('Student', back_populates='teachers')
    subject=relationship('Subject', back_populates='teachers')
