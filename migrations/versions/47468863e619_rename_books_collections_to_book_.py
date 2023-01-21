"""rename books_collections to book_collection

Revision ID: 47468863e619
Revises: fc01b4c41f4d
Create Date: 2022-06-21 15:24:01.998187

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '47468863e619'
down_revision = 'fc01b4c41f4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('collection_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_book_collection_book_id_books'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], name=op.f('fk_book_collection_collection_id_collections'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_book_collection'))
    )
    op.drop_table('books_collections')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books_collections',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('collection_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('book_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name='fk_books_collections_book_id_books', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], name='fk_books_collections_collection_id_collections', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('book_collection')
    # ### end Alembic commands ###
