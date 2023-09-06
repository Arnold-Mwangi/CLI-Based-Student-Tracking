"""Modified Relationship

Revision ID: 9edc3439db92
Revises: 382168fcff49
Create Date: 2023-09-06 20:29:36.346590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9edc3439db92'
down_revision: Union[str, None] = '382168fcff49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student_subject_association',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], name=op.f('fk_student_subject_association_student_id_students')),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], name=op.f('fk_student_subject_association_subject_id_subjects'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_subject_association')
    # ### end Alembic commands ###
