from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import generate_docs

router = APIRouter()

# Define expected request body
class CodeInput(BaseModel):
    code: str

@router.post("/")
async def auto_doc(input: CodeInput):
    generated_doc = generate_docs(input.code)
    return {"documentation": generated_doc}
