from sqlalchemy import String, Integer, PrimaryKeyConstraint,CheckConstraint, Boolean, ForeignKeyConstraint, ForeignKey, MetaData, Sequence,Column, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention= convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///bukura.db')

Session = sessionmaker(bind =  engine)

session = Session()

class Student(Base):
    __tablename__ = "students"


    student_id = Column(Integer(), primary_key =True, autoincrement=True)
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    phone_number = Column(String())



class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String())
    subject_code = Column(String())


