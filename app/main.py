from fastapi import FastAPI
from app.workflow_engine import WorkflowEngine

app = FastAPI()

workflow = WorkflowEngine()

@app.get("/")
def home():
    return {"message": "Enterprise AI Workflow Agent"}

@app.post("/run-workflow")
def run_workflow(query: str):

    result = workflow.run(query)

    return {
        "query": query,
        "result": result
    }
