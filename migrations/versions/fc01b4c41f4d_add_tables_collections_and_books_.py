"""add tables collections and books_collections

Revision ID: fc01b4c41f4d
Revises: faf57c068620
Create Date: 2022-06-21 15:22:45.834131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc01b4c41f4d'
down_revision = 'faf57c068620'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_collections_user_id_users'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_collections'))
    )
    op.create_table('books_collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('collection_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_books_collections_book_id_books'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], name=op.f('fk_books_collections_collection_id_collections'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_books_collections'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books_collections')
    op.drop_table('collections')
    # ### end Alembic commands ###