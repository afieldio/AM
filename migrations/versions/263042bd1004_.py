"""empty message

Revision ID: 263042bd1004
Revises: 35b2c3ccbb17
Create Date: 2015-09-21 12:20:31.658346

"""

# revision identifiers, used by Alembic.
revision = '263042bd1004'
down_revision = '35b2c3ccbb17'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###

    op.add_column('sensors', sa.Column('fish_temp', sa.FLOAT()))
    op.add_column('sensors', sa.Column('grow_temp', sa.FLOAT()))
    # sa.Column('grow_temp', sa.FLOAT(), 0.0))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('sensors',
    # sa.Column('pkS', sa.INTEGER(), nullable=False),
    # sa.Column('sump_temp', sa.FLOAT(), nullable=True),
    # sa.Column('air_temp', sa.FLOAT(), nullable=True),
    # sa.Column('date', sa.DATETIME(), nullable=True),
    # sa.Column('light_lux', sa.FLOAT(), nullable=True),
    # sa.PrimaryKeyConstraint('pkS')
    # )
    # op.create_table('switches',
    # sa.Column('pkSw', sa.INTEGER(), nullable=False),
    # sa.Column('waterSw', sa.BOOLEAN(), nullable=True),
    # sa.Column('airSw', sa.BOOLEAN(), nullable=True),
    # sa.Column('lightSw', sa.BOOLEAN(), nullable=True),
    # sa.Column('dateSw', sa.DATETIME(), nullable=True),
    # sa.PrimaryKeyConstraint('pkSw')
    # )

    op.drop_column('sensors', 'fish_temp')
    op.drop_column('sensors', 'grow_temp')
    ### end Alembic commands ###
