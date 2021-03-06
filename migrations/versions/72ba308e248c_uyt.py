"""uyt

Revision ID: 72ba308e248c
Revises: 
Create Date: 2017-11-01 12:50:34.635209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72ba308e248c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    op.drop_table('feedbacks')
    op.add_column('pitches', sa.Column('pitch_body', sa.String(length=255), nullable=True))
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.drop_column('pitches', 'heading')
    op.drop_column('pitches', 'body')
    op.drop_column('pitches', 'category')
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_constraint('users_pitch_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'pitch_id')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_pitch_id_fkey', 'users', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('users', 'pass_secure')
    op.add_column('pitches', sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('body', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('heading', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    op.drop_column('pitches', 'pitch_body')
    op.create_table('feedbacks',
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='feedbacks_pkey')
    )
    op.create_table('categories',
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='categories_pkey')
    )
    # ### end Alembic commands ###
