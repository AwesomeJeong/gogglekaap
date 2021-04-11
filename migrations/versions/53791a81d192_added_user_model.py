"""Added user model

Revision ID: 53791a81d192
Revises: 
Create Date: 2021-04-11 15:31:04.780921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53791a81d192'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('user_name', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###