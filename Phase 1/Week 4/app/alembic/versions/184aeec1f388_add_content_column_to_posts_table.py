"""add content column to posts table

Revision ID: 184aeec1f388
Revises: eeca4294896f
Create Date: 2026-10-10 00:34:42.925131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '184aeec1f388'
down_revision: Union[str, Sequence[str], None] = 'eeca4294896f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
