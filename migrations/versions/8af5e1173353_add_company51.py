"""add company51

Revision ID: 8af5e1173353
Revises: 5c4a5881a63a
Create Date: 2023-04-21 15:28:52.836547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8af5e1173353'
down_revision = '5c4a5881a63a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company_keywords', sa.Column('owner_email', sa.String(), nullable=False))
    op.drop_constraint('company_keywords_user_id_fkey', 'company_keywords', type_='foreignkey')
    op.create_foreign_key(None, 'company_keywords', 'user', ['owner_email'], ['email'])
    op.drop_column('company_keywords', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company_keywords', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'company_keywords', type_='foreignkey')
    op.create_foreign_key('company_keywords_user_id_fkey', 'company_keywords', 'user', ['user_id'], ['id'])
    op.drop_column('company_keywords', 'owner_email')
    # ### end Alembic commands ###
