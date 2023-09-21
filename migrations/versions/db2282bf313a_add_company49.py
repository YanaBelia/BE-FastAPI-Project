"""add company49

Revision ID: db2282bf313a
Revises: ae7dfc4aa396
Create Date: 2023-04-21 15:19:14.812542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db2282bf313a'
down_revision = 'ae7dfc4aa396'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invite', sa.Column('user_email', sa.String(), nullable=True))
    op.drop_constraint('invite_user_id_fkey', 'invite', type_='foreignkey')
    op.create_foreign_key(None, 'invite', 'user', ['user_email'], ['email'])
    op.drop_column('invite', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invite', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'invite', type_='foreignkey')
    op.create_foreign_key('invite_user_id_fkey', 'invite', 'user', ['user_id'], ['id'])
    op.drop_column('invite', 'user_email')
    # ### end Alembic commands ###