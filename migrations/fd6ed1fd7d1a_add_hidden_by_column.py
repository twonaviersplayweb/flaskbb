"""Add hidden_by column

Revision ID: fd6ed1fd7d1a
Revises: 63eabbb0e837
Create Date: 2017-09-04 13:04:52.973752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd6ed1fd7d1a'
down_revision = '63eabbb0e837'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hidden_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_Post_hidden_by', 'users', ['hidden_by_id'], ['id'])

    with op.batch_alter_table('topics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hidden_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_Topic_hidden_by', 'users', ['hidden_by_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topics', schema=None) as batch_op:
        batch_op.drop_constraint('fk_Topic_hidden_by', type_='foreignkey')
        batch_op.drop_column('hidden_by_id')

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint('fk_Post_hidden_by', type_='foreignkey')
        batch_op.drop_column('hidden_by_id')

    # ### end Alembic commands ###
