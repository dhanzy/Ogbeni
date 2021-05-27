"""empty message

Revision ID: 044063e7671b
Revises: 
Create Date: 2021-05-27 05:55:27.306555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '044063e7671b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=30), nullable=True),
    sa.Column('lastname', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('last_login_ip', sa.String(), nullable=True),
    sa.Column('current_login_ip', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('image', sa.Unicode(length=150), nullable=False),
    sa.Column('digital', sa.Boolean(), nullable=True),
    sa.Column('added_date', sa.DateTime(), nullable=True),
    sa.Column('category', sa.String(length=20), nullable=True),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=30), nullable=True),
    sa.Column('lastname', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('profile_image', sa.Unicode(length=150), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orderitem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.String(), nullable=True),
    sa.Column('products', sa.String(length=200), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('date_ordered', sa.DateTime(), nullable=True),
    sa.Column('size', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['products'], ['product.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderitem')
    op.drop_table('order')
    op.drop_table('category')
    op.drop_table('user')
    op.drop_table('product')
    op.drop_table('customer')
    # ### end Alembic commands ###
