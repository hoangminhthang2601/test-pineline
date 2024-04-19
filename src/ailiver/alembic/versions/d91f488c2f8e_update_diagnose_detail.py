"""update diagnose_detail

Revision ID: d91f488c2f8e
Revises: 8f83d131a7ac
Create Date: 2024-03-07 03:26:58.461436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd91f488c2f8e'
down_revision: Union[str, None] = '8f83d131a7ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('diagnose_details_dia_id_fkey', 'diagnose_details', type_='foreignkey')
    op.create_foreign_key(None, 'diagnose_details', 'diagnoses', ['dia_id'], ['dia_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'diagnose_details', type_='foreignkey')
    op.create_foreign_key('diagnose_details_dia_id_fkey', 'diagnose_details', 'organizations', ['dia_id'], ['org_id'])
    # ### end Alembic commands ###
