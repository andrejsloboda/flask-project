"""adds html render to article table

Revision ID: 53793d595048
Revises: f697d48028f2
Create Date: 2022-11-28 22:23:12.166655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53793d595048'
down_revision = 'f697d48028f2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("article",
            sa.Column("html_render", sa.String, server_default=""))

    
def downgrade():
    op.drop_column("article", "html_render")
