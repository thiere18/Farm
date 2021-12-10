"""creating user table

Revision ID: 066d2817d034
Revises: 
Create Date: 2021-12-09 16:35:36.676046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '066d2817d034'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():  
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("password", sa.String(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
         sa.Column('user_role', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
   
        
    # op.create_table(
    #     "roles",
    #     sa.Column("id", sa.Integer(), nullable=False),
    #     sa.Column("name", sa.String(), nullable=True),
    #     sa.Column('created_at', sa.TIMESTAMP(timezone=True),
    #                           server_default=sa.text('now()'), nullable=False),
    #     sa.PrimaryKeyConstraint("id"),

    # # )
    # op.create_unique_constraint("name_role", "roles", ["name"])

    # op.create_foreign_key('role_users_fk', source_table="users", referent_table="roles", local_cols=[
    #                       'user_role'], remote_cols=['name'], ondelete="CASCADE")





def downgrade():
    op.drop_table('users')
    op.drop_table('roles')
    pass
