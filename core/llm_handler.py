from groq import Groq
from config import API_KEY
from core.prompts import STUDENT_PROMPT, FACULTY_PROMPT

client = Groq(api_key = API_KEY)

def llm_call(role, pdf_content, question):
    system_prompt = STUDENT_PROMPT if role == "Student" else FACULTY_PROMPT
    user_prompt = f"Context Material {pdf_content} {role}'s Question: {question}"

    chat_completion = client.chat.completions.create(
            messages = [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                    }
            ],
            model="openai/gpt-oss-20b"
    )

    return chat_completion
