import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
project_id = os.getenv("OPENAI_PROJECT_ID")
organization_id = os.getenv("OPENAI_ORG_ID")

client = OpenAI(
    api_key = api_key,
    project=project_id,
    organization=organization_id
)

def generate_sql(prompt: str) -> str:
    """Generate an SQL query from a natural language prompt using OpenAI GPT."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Convert this to SQL: {prompt}"}],
        max_tokens=150,
        temperature=0.2,
    )
    print(response)
    return response.choices[0].message.content.strip()


def generate_docs(code: str) -> str:
    """Generate documentation for the provided code using OpenAI GPT."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Document this code:\n\n{code}"}],
        max_tokens=150,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


