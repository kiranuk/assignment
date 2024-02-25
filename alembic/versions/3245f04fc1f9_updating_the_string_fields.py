"""updating the string fields

Revision ID: 3245f04fc1f9
Revises: 41e3b51784d6
Create Date: 2024-02-25 10:18:33.362507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3245f04fc1f9'
down_revision: Union[str, None] = '41e3b51784d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
