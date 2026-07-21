import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.company import Company
from app.models.user import User
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.core.security import verify_password


@pytest.fixture()
def db_session():
    engine = create_engine("sqlite:///:memory:", future=True)
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


def test_user_service_create_and_authenticate(db_session):
    company = Company(name="Acme", email="acme@example.com")
    db_session.add(company)
    db_session.commit()
    db_session.refresh(company)

    service = UserService()
    user = service.create(
        db_session,
        company_id=company.id,
        name="Ana",
        email="ana@example.com",
        password="secret123",
    )

    assert user.email == "ana@example.com"
    assert verify_password("secret123", user.password_hash)

    authenticated = service.authenticate(db_session, "ana@example.com", "secret123")
    assert authenticated is not None


def test_auth_service_login_issues_tokens(db_session):
    company = Company(name="Acme", email="acme@example.com")
    db_session.add(company)
    db_session.commit()
    db_session.refresh(company)

    user_service = UserService()
    user = user_service.create(
        db_session,
        company_id=company.id,
        name="Bob",
        email="bob@example.com",
        password="secret123",
    )

    auth_service = AuthService()
    result = auth_service.login(
        db_session,
        email="bob@example.com",
        password="secret123",
        company_id=company.id,
        ip_address="127.0.0.1",
        user_agent="pytest",
    )

    assert result["access_token"]
    assert result["refresh_token"]
