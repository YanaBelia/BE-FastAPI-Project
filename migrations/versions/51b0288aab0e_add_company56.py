"""add company56

Revision ID: 51b0288aab0e
Revises: ea91537110a7
Create Date: 2023-05-15 23:53:59.318909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51b0288aab0e'
down_revision = 'ea91537110a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('users_emails', sa.String(), nullable=True))
    op.create_index(op.f('ix_company_users_emails'), 'company', ['users_emails'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_company_users_emails'), table_name='company')
    op.drop_column('company', 'users_emails')
    # ### end Alembic commands ###
