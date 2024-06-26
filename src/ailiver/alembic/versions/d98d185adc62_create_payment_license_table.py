"""create payment license table

Revision ID: d98d185adc62
Revises: df9588869eab
Create Date: 2024-03-07 03:19:49.915305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd98d185adc62'
down_revision: Union[str, None] = 'df9588869eab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('licenses',
    sa.Column('license_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=True),
    sa.Column('payment_id', sa.Integer(), nullable=True),
    sa.Column('is_activate', sa.Boolean(), nullable=True),
    sa.Column('start_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('end_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['org_id'], ['organizations.org_id'], ),
    sa.ForeignKeyConstraint(['payment_id'], ['payments.payment_id'], ),
    sa.PrimaryKeyConstraint('license_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('licenses')
    # ### end Alembic commands ###
