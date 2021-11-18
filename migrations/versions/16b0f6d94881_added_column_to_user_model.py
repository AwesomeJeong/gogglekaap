"""Added column to user model

Revision ID: 16b0f6d94881
Revises: 04af6c17c9f2
Create Date: 2021-11-18 11:47:50.082063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16b0f6d94881'
down_revision = '04af6c17c9f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_at')
    # ### end Alembic commands ###