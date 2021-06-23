"""create categories, countries, shops, users and usertiers table

Revision ID: db2d755431b5
Revises: 
Create Date: 2021-06-14 14:04:41.487248

"""
from models.countries import Country
from models.categories import Category
from models.usertier import UserTier
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column, ForeignKey
# from sqlalchemy import Column, Integer, Float, String


# revision identifiers, used by Alembic.
revision = 'db2d755431b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(300), nullable=False),
        sa.Column('logo', sa.String(150), nullable=False)
    )
    op.create_table(
        'countries',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('code', sa.String(3), nullable=False)
    )
    op.create_table(
        'shops',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('description', sa.String(300), nullable=False),
        sa.Column('cashback_percentage', sa.Float, nullable=False),
        sa.Column('logo', sa.String(150), nullable=False),
        sa.Column('category_id', sa.Integer, ForeignKey(Category.id), nullable=False),
    )
    op.create_table(
        'usertiers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True, index=True),
        sa.Column('min_points', sa.Integer, nullable=False),
        sa.Column('max_points', sa.Integer, nullable=False),
        sa.Column('cashback_multiplier', sa.Float, nullable=False),
        sa.Column('reward_time', sa.Float, nullable=False)
    )
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(20), nullable=False, unique=True, index=True),
        sa.Column('email', sa.String(50), nullable=False, unique=True, index=True),
        sa.Column('password', sa.String(100), nullable=False),
        sa.Column('status', sa.SmallInteger, nullable=False),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('phone', sa.String(30), nullable=True),
        sa.Column('profile_image', sa.String(150), nullable=True),
        sa.Column('balance', sa.BigInteger, nullable=False),
        sa.Column('user_tier_id', sa.Integer, ForeignKey(UserTier.id), nullable=False),
        sa.Column('country_id', sa.Integer, ForeignKey(Country.id), nullable=False)
    )

def downgrade():
    op.drop_table('categories')
    op.drop_table('countries')
    op.drop_table('shops')
    op.drop_table('users')
    op.drop_table('usertiers')
