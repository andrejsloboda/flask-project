"""Adds newsletter

Revision ID: e93aead434b1
Revises: 53793d595048
Create Date: 2022-11-30 22:29:45.373879

"""
from alembic import op
import sqlalchemy as sa

 
# revision identifiers, used by Alembic.
revision = 'e93aead434b1'
down_revision = '53793d595048'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "newsletter",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, unique=True))


def downgrade():
    op.drop_table("newsletter")
