# In app/routes/auto_doc.py
from fastapi import APIRouter, Body
from app.services.llm_service import generate_docs

router = APIRouter()

@router.post("/")
async def auto_doc(code: str = Body(...)):
    # Call the function to generate documentation from code
    generated_doc = generate_docs(code)
    return {"documentation": generated_doc}
