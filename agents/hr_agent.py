from app.workflow_engine import run_workflow
from app.planner import plan_task

def run(query):
    plan = plan_task(query)
    return run_workflow(plan)
