"""add company45

Revision ID: 2fb8dfdc9dce
Revises: 
Create Date: 2023-04-21 14:03:51.502089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fb8dfdc9dce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('is_visible', sa.Boolean(), nullable=True),
    sa.Column('owner_email', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['owner_email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_description'), 'company', ['description'], unique=False)
    op.create_index(op.f('ix_company_id'), 'company', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_company_id'), table_name='company')
    op.drop_index(op.f('ix_company_description'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
