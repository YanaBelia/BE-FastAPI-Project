"""add company54

Revision ID: 9c433a6aad36
Revises: f36bd44c4f58
Create Date: 2023-05-15 02:04:50.493438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c433a6aad36'
down_revision = 'f36bd44c4f58'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invite', sa.Column('user', sa.String(), nullable=True))
    op.create_index(op.f('ix_invite_user'), 'invite', ['user'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_invite_user'), table_name='invite')
    op.drop_column('invite', 'user')
    # ### end Alembic commands ###