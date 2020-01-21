"""empty message

Revision ID: cbb9e751bd5c
Revises: 7983a11a4f35
Create Date: 2020-02-04 05:46:44.853961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbb9e751bd5c'
down_revision = '7983a11a4f35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lang', sa.String(length=128), nullable=False),
    sa.Column('localization', sa.String(length=128), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_content_timestamp'), 'content', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_content_timestamp'), table_name='content')
    op.drop_table('content')
    # ### end Alembic commands ###
