"""update column name

Revision ID: d08a8af60e61
Revises: 7592ebde6af9
Create Date: 2021-11-18 17:07:09.757070

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd08a8af60e61'
down_revision = '7592ebde6af9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('isMngmnt', sa.Boolean(), nullable=True))
    op.drop_column('item', 'isMngmt')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('isMngmt', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('item', 'isMngmnt')
    # ### end Alembic commands ###