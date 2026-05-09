from fastapi import APIRouter
from app.planner import plan_task
from app.workflow_engine import run_workflow

router = APIRouter()

@router.post("/agent/run")
async def run_agent(query: str):
    # 1. 任务拆解
    plan = plan_task(query)

    # 2. workflow执行
    result = run_workflow(plan)

    return {
        "plan": plan,
        "result": result
    }
