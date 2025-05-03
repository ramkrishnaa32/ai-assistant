from pydantic import BaseModel
from fastapi import APIRouter
from app.services.llm_service import generate_sql

router = APIRouter()

class SQLRequest(BaseModel):
    prompt: str

@router.post("/")
async def sql_assistant(request: SQLRequest):
    result = generate_sql(request.prompt)
    return {"sql": result}
