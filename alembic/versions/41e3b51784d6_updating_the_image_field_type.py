"""updating the image field type

Revision ID: 41e3b51784d6
Revises: 97e1a94cb069
Create Date: 2024-02-25 00:49:01.500772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41e3b51784d6'
down_revision: Union[str, None] = '97e1a94cb069'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
