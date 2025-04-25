import os
import openai
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, set_seed
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize generator pipeline
model_id = "Salesforce/codegen-350M-multi"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)
set_seed(42)

# def generate_sql(prompt: str) -> str:
#     """Generate an SQL query from a natural language prompt using OpenAI GPT."""
#     response = openai.completions.create(
#         model="gpt-3.5-turbo",
#         prompt=f"Convert this to SQL: {prompt}",
#         max_tokens=150,
#         temperature=0.2,
#     )
#     print(response)
#     return response['choices'][0]['text'].strip()
#
# def generate_docs(code: str) -> str:
#     """Generate documentation for the provided code using OpenAI GPT."""
#     response = openai.completions.create(
#         model="gpt-3.5-turbo",
#         prompt=f"Document this code:\n\n{code}",
#         max_tokens=150,
#         temperature=0.3,
#     )
#     return response['choices'][0]['text'].strip()

def generate_sql(prompt: str) -> str:
    input_text = f"-- Natural Language: {prompt}\n-- SQL:\n"
    output = generator(input_text, max_length=150, do_sample=True, temperature=0.5, truncation=True)
    return output[0]["generated_text"].replace(input_text, "").strip()

def generate_docs(code: str) -> str:
    input_text = f"# Code:\n{code}\n# Documentation:\n"
    output = generator(input_text, max_length=200, do_sample=True, temperature=0.5, truncation=True)
    return output[0]["generated_text"].replace(input_text, "").strip()