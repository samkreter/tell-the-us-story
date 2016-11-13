"""empty message

Revision ID: d32cc8c8df49
Revises: 30d3a6989c9c
Create Date: 2016-11-13 14:22:18.052953

"""

# revision identifiers, used by Alembic.
revision = 'd32cc8c8df49'
down_revision = '30d3a6989c9c'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'timestamp')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
