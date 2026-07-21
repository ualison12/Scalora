"""add_crm_models

Revision ID: 0d1c6f5a2d4b
Revises: fe4296b7029d
Create Date: 2026-07-21 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0d1c6f5a2d4b"
down_revision = "fe4296b7029d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "crm_leads",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("phone", sa.String(length=50), nullable=True),
        sa.Column("source", sa.String(length=100), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_crm_leads_company_id"), "crm_leads", ["company_id"], unique=False)
    op.create_index(op.f("ix_crm_leads_id"), "crm_leads", ["id"], unique=False)

    op.create_table(
        "crm_contacts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("phone", sa.String(length=50), nullable=True),
        sa.Column("job_title", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_crm_contacts_company_id"), "crm_contacts", ["company_id"], unique=False)
    op.create_index(op.f("ix_crm_contacts_id"), "crm_contacts", ["id"], unique=False)

    op.create_table(
        "crm_stages",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("position", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_crm_stages_company_id"), "crm_stages", ["company_id"], unique=False)
    op.create_index(op.f("ix_crm_stages_id"), "crm_stages", ["id"], unique=False)

    op.create_table(
        "crm_deals",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=1000), nullable=True),
        sa.Column("amount", sa.Float(), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.ForeignKeyConstraint(["stage_id"], ["crm_stages.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_crm_deals_company_id"), "crm_deals", ["company_id"], unique=False)
    op.create_index(op.f("ix_crm_deals_id"), "crm_deals", ["id"], unique=False)
    op.create_index(op.f("ix_crm_deals_stage_id"), "crm_deals", ["stage_id"], unique=False)

    op.create_table(
        "crm_activities",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("type", sa.String(length=100), nullable=False),
        sa.Column("notes", sa.String(length=1000), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_crm_activities_company_id"), "crm_activities", ["company_id"], unique=False)
    op.create_index(op.f("ix_crm_activities_id"), "crm_activities", ["id"], unique=False)

    op.create_table(
        "crm_notes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("content", sa.String(length=2000), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_crm_notes_company_id"), "crm_notes", ["company_id"], unique=False)
    op.create_index(op.f("ix_crm_notes_id"), "crm_notes", ["id"], unique=False)

    op.create_table(
        "crm_tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("completed", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_crm_tasks_company_id"), "crm_tasks", ["company_id"], unique=False)
    op.create_index(op.f("ix_crm_tasks_id"), "crm_tasks", ["id"], unique=False)


def downgrade() -> None:
    op.drop_table("crm_tasks")
    op.drop_table("crm_notes")
    op.drop_table("crm_activities")
    op.drop_table("crm_deals")
    op.drop_table("crm_stages")
    op.drop_table("crm_contacts")
    op.drop_table("crm_leads")
