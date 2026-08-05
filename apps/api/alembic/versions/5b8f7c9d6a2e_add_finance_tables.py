"""add_finance_tables

Revision ID: 5b8f7c9d6a2e
Revises: 0d1c6f5a2d4b
Create Date: 2026-08-04 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "5b8f7c9d6a2e"
down_revision = "0d1c6f5a2d4b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "finance_categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("kind", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_finance_categories_company_id"), "finance_categories", ["company_id"], unique=False)
    op.create_index(op.f("ix_finance_categories_id"), "finance_categories", ["id"], unique=False)

    op.create_table(
        "finance_cost_centers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("code", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_finance_cost_centers_company_id"), "finance_cost_centers", ["company_id"], unique=False)
    op.create_index(op.f("ix_finance_cost_centers_id"), "finance_cost_centers", ["id"], unique=False)

    op.create_table(
        "finance_payables",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=True),
        sa.Column("cost_center_id", sa.Integer(), nullable=True),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("amount", sa.Float(), nullable=True),
        sa.Column("due_date", sa.Date(), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["category_id"], ["finance_categories.id"]),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.ForeignKeyConstraint(["cost_center_id"], ["finance_cost_centers.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_finance_payables_company_id"), "finance_payables", ["company_id"], unique=False)
    op.create_index(op.f("ix_finance_payables_id"), "finance_payables", ["id"], unique=False)
    op.create_index(op.f("ix_finance_payables_category_id"), "finance_payables", ["category_id"], unique=False)
    op.create_index(op.f("ix_finance_payables_cost_center_id"), "finance_payables", ["cost_center_id"], unique=False)

    op.create_table(
        "finance_receivables",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=True),
        sa.Column("cost_center_id", sa.Integer(), nullable=True),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("amount", sa.Float(), nullable=True),
        sa.Column("due_date", sa.Date(), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["category_id"], ["finance_categories.id"]),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.ForeignKeyConstraint(["cost_center_id"], ["finance_cost_centers.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_finance_receivables_company_id"), "finance_receivables", ["company_id"], unique=False)
    op.create_index(op.f("ix_finance_receivables_id"), "finance_receivables", ["id"], unique=False)
    op.create_index(op.f("ix_finance_receivables_category_id"), "finance_receivables", ["category_id"], unique=False)
    op.create_index(op.f("ix_finance_receivables_cost_center_id"), "finance_receivables", ["cost_center_id"], unique=False)

    op.create_table(
        "finance_pix",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("transaction_id", sa.Integer(), nullable=True),
        sa.Column("amount", sa.Float(), nullable=True),
        sa.Column("code", sa.String(length=100), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_finance_pix_company_id"), "finance_pix", ["company_id"], unique=False)
    op.create_index(op.f("ix_finance_pix_id"), "finance_pix", ["id"], unique=False)

    op.create_table(
        "finance_boletos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("transaction_id", sa.Integer(), nullable=True),
        sa.Column("amount", sa.Float(), nullable=True),
        sa.Column("code", sa.String(length=100), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_finance_boletos_company_id"), "finance_boletos", ["company_id"], unique=False)
    op.create_index(op.f("ix_finance_boletos_id"), "finance_boletos", ["id"], unique=False)


def downgrade() -> None:
    op.drop_table("finance_boletos")
    op.drop_table("finance_pix")
    op.drop_table("finance_receivables")
    op.drop_table("finance_payables")
    op.drop_table("finance_cost_centers")
    op.drop_table("finance_categories")
