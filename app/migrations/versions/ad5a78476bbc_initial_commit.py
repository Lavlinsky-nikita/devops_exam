"""initial commit

Revision ID: ad5a78476bbc
Revises: 
Create Date: 2023-01-21 16:30:33.880485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad5a78476bbc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_table1'))
    )
    op.create_table('table2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_table2'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('middle_name', sa.String(length=100), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('login', name=op.f('uq_users_login')),
    sa.UniqueConstraint('password_hash', name=op.f('uq_users_password_hash'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('table2')
    op.drop_table('table1')
    # ### end Alembic commands ###