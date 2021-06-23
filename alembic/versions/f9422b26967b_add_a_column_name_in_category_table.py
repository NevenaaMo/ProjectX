"""Add a column name in category table

Revision ID: f9422b26967b
Revises: db2d755431b5
Create Date: 2021-06-17 13:35:03.740076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9422b26967b'
down_revision = 'db2d755431b5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('categories', sa.Column('name', sa.String(50), nullable=False))

def downgrade():
    op.drop_column('categories', 'name')
