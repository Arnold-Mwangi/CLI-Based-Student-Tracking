from sqlalchemy import String, Integer, PrimaryKeyConstraint,CheckConstraint, Boolean, ForeignKeyConstraint, ForeignKey, MetaData, Sequence,Column, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention= convention)

Base = declarative_base(metadata=metadata)


class Student(Base):
    __tablename__ = "students"


    student_id = Column(Integer(), primary_key =True, server_default = text("CONCAT('GOK/', YEAR(CURRENT_DATE), '/', nextval('student_id_seq'))"))
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    phone_number = Column(Integer())

student_id_seq = Sequence('student_id_seq')


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String())
    subject_code = Column(String())


