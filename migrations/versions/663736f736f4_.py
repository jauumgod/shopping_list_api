"""empty message

Revision ID: 663736f736f4
Revises: 
Create Date: 2023-09-08 10:22:07.180718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '663736f736f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tab_produtos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('quantidade', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tab_shoppinglist',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.Integer(), nullable=True),
    sa.Column('date_create', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tab_usuarios',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('senha', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tab_history',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.Column('quantidade_id', sa.Integer(), nullable=True),
    sa.Column('data_compra', sa.TIMESTAMP(), nullable=True),
    sa.Column('usuario_id_key', sa.Integer(), nullable=True),
    sa.Column('produto_id_key', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['produto_id_key'], ['tab_produtos.id'], ),
    sa.ForeignKeyConstraint(['usuario_id_key'], ['tab_usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tab_produtos_list',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lista_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('lista_id_key', sa.Integer(), nullable=True),
    sa.Column('produto_id_key', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lista_id_key'], ['tab_shoppinglist.id'], ),
    sa.ForeignKeyConstraint(['produto_id_key'], ['tab_produtos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tab_produtos_list')
    op.drop_table('tab_history')
    op.drop_table('tab_usuarios')
    op.drop_table('tab_shoppinglist')
    op.drop_table('tab_produtos')
    # ### end Alembic commands ###
