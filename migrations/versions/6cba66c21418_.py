"""empty message

Revision ID: 6cba66c21418
Revises: 33b8ad3507ff
Create Date: 2019-10-09 21:59:57.085929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cba66c21418'
down_revision = '33b8ad3507ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'))
    op.execute("insert into todolists (name) values ('uncategorized')")
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.execute("update todos set list_id=1")
    op.alter_column('todos', 'list_id', nullable=False)
    op.create_foreign_key(u'list_id_fkey', 'todos',
                          'todolists', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'list_id_fkey', 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolists')
    # ### end Alembic commands ###
