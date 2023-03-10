"""del users

Revision ID: 1f434913ea48
Revises: c68136ed6270
Create Date: 2023-01-25 12:11:50.058681

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1f434913ea48'
down_revision = 'c68136ed6270'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('uq_users_login')
        batch_op.drop_index('uq_users_password_hash')

    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('middle_name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('login', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('uq_users_password_hash', ['password_hash'], unique=False)
        batch_op.create_index('uq_users_login', ['login'], unique=False)

    # ### end Alembic commands ###
