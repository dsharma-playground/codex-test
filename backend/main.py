from fastapi import FastAPI

app = FastAPI(title="Agent Governance API")

@app.get("/agents")
async def list_agents():
    """List configured agents (placeholder)."""
    return {"agents": []}

@app.post("/agents")
async def create_agent(agent: dict):
    """Create a new agent (placeholder)."""
    return {"message": "Agent created", "agent": agent}

