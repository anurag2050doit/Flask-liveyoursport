"""empty message

Revision ID: babb1f1f8860
Revises: 
Create Date: 2017-04-02 10:26:22.840726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'babb1f1f8860'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.String(length=20), nullable=True),
    sa.Column('product_name', sa.String(length=200), nullable=True),
    sa.Column('order_status', sa.String(length=10), nullable=True),
    sa.Column('product_url', sa.String(length=150), nullable=True),
    sa.Column('cost_price', sa.Float(), nullable=True),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###
