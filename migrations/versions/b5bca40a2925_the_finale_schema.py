"""the finale schema

Revision ID: b5bca40a2925
Revises: 9d229c9c7d17
Create Date: 2024-02-26 21:07:33.878770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5bca40a2925'
down_revision = '9d229c9c7d17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('account_number', sa.String(), nullable=True),
    sa.Column('account_type', sa.String(), nullable=True),
    sa.Column('balance', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('opened_at', sa.DateTime(), nullable=True),
    sa.Column('closed_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loan_applications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('loan_type', sa.String(), nullable=True),
    sa.Column('amount_requested', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('interest_rate', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('monthly_payment', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('submitted_at', sa.DateTime(), nullable=True),
    sa.Column('reviewed_by', sa.String(), nullable=True),
    sa.Column('reviewed_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('transaction_type', sa.String(), nullable=True),
    sa.Column('related_transaction_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('initiated_by', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('user_profiles')
    op.drop_table('loan_applications')
    op.drop_table('accounts')
    # ### end Alembic commands ###