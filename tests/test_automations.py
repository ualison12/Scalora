import sys
from pathlib import Path

# Adiciona o diretório 'apps/api' ao sys.path para que 'app' seja importável
api_dir = Path(__file__).resolve().parent.parent / "apps" / "api"
if str(api_dir) not in sys.path:
    sys.path.insert(0, str(api_dir))

import pytest
from app.modules.automations.engine.schemas import FlowDefinition, FlowNode, FlowEdge, NodeType
from app.modules.automations.engine.executor import FlowExecutor

@pytest.mark.asyncio
async def test_flow_execution_with_delay_and_action():
    flow = FlowDefinition(
        id="flow_001",
        name="Boas vindas WhatsApp",
        active=True,
        nodes=[
            FlowNode(id="node_1", type=NodeType.TRIGGER, handler="event.webhook_received"),
            FlowNode(id="node_2", type=NodeType.DELAY, handler="delay.wait", config={"seconds": 0}),
            FlowNode(id="node_3", type=NodeType.ACTION, handler="whatsapp.send", config={"phone": "5531999999999", "message": "Ola!"})
        ],
        edges=[
            FlowEdge(id="e1", source="node_1", target="node_2"),
            FlowEdge(id="e2", source="node_2", target="node_3")
        ]
    )

    executor = FlowExecutor()
    result = await executor.execute_flow(flow, initial_context={"lead_name": "Ualison"})

    assert result["status"] == "completed"
    assert "node_3" in result["final_context"]
    assert result["final_context"]["node_3"]["status"] == "sent"
