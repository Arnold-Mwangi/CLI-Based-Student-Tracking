"""Create Attendance MOdel

Revision ID: adc08c60b997
Revises: 88c6f01516c7
Create Date: 2023-09-07 12:28:41.755044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adc08c60b997'
down_revision: Union[str, None] = '88c6f01516c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attendances',
    sa.Column('attendance_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('attendance_date', sa.DateTime(), nullable=True),
    sa.Column('checkin_time', sa.DateTime(), nullable=True),
    sa.Column('checkout_time', sa.DateTime(), nullable=True),
    sa.Column('attendance_status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], name=op.f('fk_attendances_student_id_students')),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], name=op.f('fk_attendances_subject_id_subjects')),
    sa.PrimaryKeyConstraint('attendance_id')
    )
    op.create_table('grades',
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('grade_value', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], name=op.f('fk_grades_student_id_students')),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], name=op.f('fk_grades_subject_id_subjects')),
    sa.PrimaryKeyConstraint('grade_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grades')
    op.drop_table('attendances')
    # ### end Alembic commands ###
