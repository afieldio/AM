"""empty message

Revision ID: 4558aaecbd92
Revises: 527e6dfb7259
Create Date: 2015-06-04 20:41:57.318732

"""

# revision identifiers, used by Alembic.
revision = '4558aaecbd92'
down_revision = '527e6dfb7259'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'sensors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('sump_temp', sa.Float(2), nullable=True),
        sa.Column('air_temp', sa.Float(2), nullable=True),
        sa.Column('date', sa.DateTime, nullable=False),
    )
    pass
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sensors')
    pass
    ### end Alembic commands ###