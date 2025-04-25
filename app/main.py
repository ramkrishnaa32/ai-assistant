# In app/main.py
from fastapi import FastAPI
from app.routes import sql_assistant, auto_doc

app = FastAPI()

# Include the routers
app.include_router(sql_assistant.router, prefix="/sql-assistant", tags=["SQL Assistant"])
app.include_router(auto_doc.router, prefix="/auto-doc", tags=["Auto-Doc Assistant"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the GenAI SQL + Auto-Doc Assistant API!"}
