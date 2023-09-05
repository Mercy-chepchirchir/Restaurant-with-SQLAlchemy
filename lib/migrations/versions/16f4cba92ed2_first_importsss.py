"""first importsss

Revision ID: 16f4cba92ed2
Revises: cd22425afd3e
Create Date: 2023-09-05 11:21:02.375711

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16f4cba92ed2'
down_revision: Union[str, None] = 'cd22425afd3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
