from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database import Base
from app.models.company import Company
from app.modules.ai.services.ai_service import AIService


def create_test_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)()


def test_ai_services_workflow() -> None:
    db = create_test_session()
    try:
        company = Company(name="Acme AI", email="ai@example.com")
        db.add(company)
        db.commit()
        db.refresh(company)

        service = AIService()
        provider = service.configure_provider(
            db,
            company_id=company.id,
            provider_name="openai",
            api_key="demo-key",
            model_name="gpt-4o",
        )
        agent = service.create_agent(db, company_id=company.id, name="Analista", provider="claude", model="claude-3")
        prompt = service.create_prompt_template(db, company_id=company.id, name="Resumo", template="Resuma: {text}")
        tool = service.create_tool(db, company_id=company.id, name="Busca de documentos", tool_type="rag")
        automation = service.create_automation(db, company_id=company.id, name="Resumo diário", trigger="schedule", action="summarize")
        memory = service.store_memory(db, company_id=company.id, agent_id=agent.id, content="Cliente prefere respostas curtas", kind="preference")
        document = service.create_document(db, company_id=company.id, title="Política", content="Resposta curta e objetiva", source="manual")
        chat = service.send_chat(db, company_id=company.id, provider=provider.provider_name, prompt="Explique o módulo de IA", context=[memory.content, document.content])
        summary = service.summarize_text("O faturamento subiu e as vendas cresceram")
        analysis = service.analyze_text("O cliente está satisfeito e recomenda a plataforma")
        dashboard = service.get_dashboard(db, company_id=company.id)

        assert provider.provider_name == "openai"
        assert agent.name == "Analista"
        assert prompt.name == "Resumo"
        assert tool.name == "Busca de documentos"
        assert automation.name == "Resumo diário"
        assert chat["provider"] == "openai"
        assert "IA" in chat["response"]
        assert summary["summary"].startswith("Resumo")
        assert analysis["sentiment"] == "positivo"
        assert dashboard["providers_enabled"] == 1
        assert dashboard["agents_count"] == 1
        assert dashboard["documents_count"] == 1
    finally:
        db.close()
