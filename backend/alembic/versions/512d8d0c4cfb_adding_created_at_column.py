"""adding created_at column

Revision ID: 512d8d0c4cfb
Revises: 5bed873cd4c0
Create Date: 2021-12-08 17:13:27.167635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '512d8d0c4cfb'
down_revision = '5bed873cd4c0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users",  sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),)

    pass


def downgrade():
    pass
