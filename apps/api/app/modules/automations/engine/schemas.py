from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from enum import Enum

class NodeType(str, Enum):
    TRIGGER = "trigger"
    ACTION = "action"
    CONDITION = "condition"
    DELAY = "delay"

class FlowNode(BaseModel):
    id: str
    type: NodeType
    handler: str
    config: Dict[str, Any] = Field(default_factory=dict)
    position: Optional[Dict[str, float]] = None

class FlowEdge(BaseModel):
    id: str
    source: str
    target: str
    condition_value: Optional[bool] = None

class FlowDefinition(BaseModel):
    id: str
    name: str
    active: bool = True
    nodes: List[FlowNode]
    edges: List[FlowEdge]
