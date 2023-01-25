"""add tables

Revision ID: 3fb8a66500ed
Revises: ad5a78476bbc
Create Date: 2023-01-25 11:44:46.330159

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3fb8a66500ed'
down_revision = 'ad5a78476bbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('id_doctor', sa.Integer(), nullable=False),
    sa.Column('fio', sa.String(length=100), nullable=False),
    sa.Column('work_time', sa.String(length=100), nullable=False),
    sa.Column('specialisation', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id_doctor', name=op.f('pk_doctors'))
    )
    op.create_table('records',
    sa.Column('id_record', sa.Integer(), nullable=False),
    sa.Column('telephone', sa.String(length=8), nullable=False),
    sa.Column('code_sms', sa.String(length=8), nullable=False),
    sa.Column('id_doctor', sa.Integer(), nullable=False),
    sa.Column('time_record', sa.String(length=8), nullable=False),
    sa.ForeignKeyConstraint(['id_doctor'], ['doctors.id_doctor'], name=op.f('fk_records_id_doctor_doctors')),
    sa.PrimaryKeyConstraint('id_record', name=op.f('pk_records'))
    )
    op.drop_table('table1')
    op.drop_table('table2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table2',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('table1',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('records')
    op.drop_table('doctors')
    # ### end Alembic commands ###
