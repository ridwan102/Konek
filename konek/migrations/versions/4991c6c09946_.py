"""empty message

Revision ID: 4991c6c09946
Revises: 0013c6a96e6b
Create Date: 2019-08-18 21:32:58.099191

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4991c6c09946'
down_revision = '0013c6a96e6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user',
                  sa.Column('test', sa.VARCHAR(length=50), nullable=True))
    # ### end Alembic commands ###
