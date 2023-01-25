"""fix tel

Revision ID: c68136ed6270
Revises: 3fb8a66500ed
Create Date: 2023-01-25 11:58:40.380160

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c68136ed6270'
down_revision = '3fb8a66500ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('records', schema=None) as batch_op:
        batch_op.alter_column('telephone',
               existing_type=mysql.VARCHAR(length=8),
               type_=sa.String(length=16),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('records', schema=None) as batch_op:
        batch_op.alter_column('telephone',
               existing_type=sa.String(length=16),
               type_=mysql.VARCHAR(length=8),
               existing_nullable=False)

    # ### end Alembic commands ###
