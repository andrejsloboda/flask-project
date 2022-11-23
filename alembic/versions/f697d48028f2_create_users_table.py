"""Create users table

Revision ID: f697d48028f2
Revises: 
Create Date: 2022-11-23 20:03:40.584127

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f697d48028f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "user",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("username", sa.String),
            sa.Column("password", sa.String))


def downgrade():
    op.drop_table("user")
