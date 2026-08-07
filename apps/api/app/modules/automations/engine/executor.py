import logging
from typing import Dict, Any, Optional
from app.modules.automations.engine.schemas import FlowDefinition, NodeType
from app.modules.automations.actions.registry import ActionRegistry

logger = logging.getLogger("AutomationEngine")

class FlowExecutor:
    def __init__(self, action_registry: Optional[ActionRegistry] = None):
        self.registry = action_registry or ActionRegistry()

    async def execute_flow(self, flow: FlowDefinition, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        if not flow.active:
            logger.info(f"Fluxo {flow.id} ignorado pois está inativo.")
            return {"status": "skipped", "reason": "flow_inactive"}

        start_node = next((n for n in flow.nodes if n.type == NodeType.TRIGGER), None)
        if not start_node:
            raise ValueError(f"O fluxo {flow.id} não contém um nó de Trigger válido.")

        context = dict(initial_context)
        current_node = start_node

        while current_node:
            logger.info(f"Executando nó {current_node.id} ({current_node.handler})")
            
            if current_node.type in (NodeType.ACTION, NodeType.DELAY):
                handler = self.registry.get(current_node.handler)
                output = await handler(current_node.config, context)
                context[f"node_{current_node.id}"] = output
                context.update(output)

            elif current_node.type == NodeType.CONDITION:
                cond_key = current_node.config.get("key")
                expected_val = current_node.config.get("value")
                actual_val = context.get(cond_key)
                
                eval_result = (actual_val == expected_val)
                context["last_condition_result"] = eval_result

            current_node = self._get_next_node(flow, current_node, context)

        return {"status": "completed", "final_context": context}

    def _get_next_node(self, flow: FlowDefinition, current_node, context: Dict[str, Any]):
        outgoing_edges = [e for e in flow.edges if e.source == current_node.id]
        if not outgoing_edges:
            return None

        if current_node.type == NodeType.CONDITION:
            cond_res = context.get("last_condition_result", True)
            target_edge = next((e for e in outgoing_edges if e.condition_value == cond_res), None)
            if target_edge:
                return next((n for n in flow.nodes if n.id == target_edge.target), None)
            return None

        next_node_id = outgoing_edges[0].target
        return next((n for n in flow.nodes if n.id == next_node_id), None)
