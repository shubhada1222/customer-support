from langgraph.graph import StateGraph, END

from state import SupportState

from nodes.analyze import analyze_issue
from nodes.respond import generate_response


# Create Graph Builder
builder = StateGraph(SupportState)


# Add Nodes
builder.add_node(
    "analyze_issue",
    analyze_issue
)

builder.add_node(
    "generate_response",
    generate_response
)


# Set Entry Point
builder.set_entry_point("analyze_issue")
# this I have added

# Create Edges
builder.add_edge(
    "analyze_issue",
    "generate_response"
)

builder.add_edge(
    "generate_response",
    END
)


# Compile Graph
graph = builder.compile()