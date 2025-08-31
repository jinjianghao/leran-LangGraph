from typing import Dict,TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict): # Our state schema
    message: str

def greeting_node(state: AgentState) -> AgentState:
    """
    Simple node that adds a greeting message to the state.
    """
    state['message'] = "Hey " + state['message'] + ",how is your going?"
    
    return state