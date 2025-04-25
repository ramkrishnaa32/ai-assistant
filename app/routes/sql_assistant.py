# In app/routes/sql_assistant.py
from fastapi import APIRouter, Body
from app.services.llm_service import generate_sql

router = APIRouter()

@router.post("/")
async def sql_assistant(prompt: str = Body(...)):
    # Call the function to generate SQL from prompt
    generated_sql = generate_sql(prompt)
    return {"sql": generated_sql}
