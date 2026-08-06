from typing import Optional

from sqlalchemy.orm import Session

from app.modules.ai.models.agent import AIAgent
from app.modules.ai.models.automation import AIAutomation
from app.modules.ai.models.document import AIDocument
from app.modules.ai.models.memory import AIMemory
from app.modules.ai.models.prompt import PromptTemplate
from app.modules.ai.models.provider import AIProvider
from app.modules.ai.models.tool import AITool


class AIService:
    def configure_provider(
        self,
        db: Session,
        *,
        company_id: int,
        provider_name: str,
        api_key: str,
        model_name: str,
        enabled: bool = True,
    ) -> AIProvider:
        provider = AIProvider(company_id=company_id, provider_name=provider_name, api_key=api_key, model_name=model_name, enabled=1 if enabled else 0)
        db.add(provider)
        db.commit()
        db.refresh(provider)
        return provider

    def create_agent(self, db: Session, *, company_id: int, name: str, provider: str, model: str) -> AIAgent:
        agent = AIAgent(company_id=company_id, name=name, provider=provider, model=model)
        db.add(agent)
        db.commit()
        db.refresh(agent)
        return agent

    def create_prompt_template(self, db: Session, *, company_id: int, name: str, template: str) -> PromptTemplate:
        prompt = PromptTemplate(company_id=company_id, name=name, template=template)
        db.add(prompt)
        db.commit()
        db.refresh(prompt)
        return prompt

    def create_tool(self, db: Session, *, company_id: int, name: str, tool_type: str) -> AITool:
        tool = AITool(company_id=company_id, name=name, tool_type=tool_type)
        db.add(tool)
        db.commit()
        db.refresh(tool)
        return tool

    def create_automation(self, db: Session, *, company_id: int, name: str, trigger: str, action: str) -> AIAutomation:
        automation = AIAutomation(company_id=company_id, name=name, trigger=trigger, action=action)
        db.add(automation)
        db.commit()
        db.refresh(automation)
        return automation

    def store_memory(self, db: Session, *, company_id: int, agent_id: Optional[int], content: str, kind: str = "memory") -> AIMemory:
        memory = AIMemory(company_id=company_id, agent_id=agent_id, content=content, kind=kind)
        db.add(memory)
        db.commit()
        db.refresh(memory)
        return memory

    def create_document(self, db: Session, *, company_id: int, title: str, content: str, source: str) -> AIDocument:
        document = AIDocument(company_id=company_id, title=title, content=content, source=source)
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    def send_chat(self, db: Session, *, company_id: int, provider: str, prompt: str, context: Optional[list[str]] = None) -> dict[str, object]:
        context_text = "\n".join(context or [])
        response = f"Resposta IA via {provider}: {prompt}"
        if context_text:
            response = f"{response} | contexto: {context_text}"
        return {"provider": provider, "response": response, "company_id": company_id}

    def summarize_text(self, text: str) -> dict[str, str]:
        return {"summary": f"Resumo: {text}", "length": str(len(text.split()))}

    def analyze_text(self, text: str) -> dict[str, str]:
        sentiment = "positivo" if "satisfeito" in text.lower() or "cresceu" in text.lower() else "neutro"
        return {"sentiment": sentiment, "insight": f"Análise de sentimento para: {text}"}

    def get_dashboard(self, db: Session, *, company_id: int) -> dict[str, int]:
        providers_enabled = db.query(AIProvider).filter(AIProvider.company_id == company_id, AIProvider.enabled == 1).count()
        agents_count = db.query(AIAgent).filter(AIAgent.company_id == company_id).count()
        documents_count = db.query(AIDocument).filter(AIDocument.company_id == company_id).count()
        memories_count = db.query(AIMemory).filter(AIMemory.company_id == company_id).count()
        return {
            "providers_enabled": providers_enabled,
            "agents_count": agents_count,
            "documents_count": documents_count,
            "memories_count": memories_count,
        }
