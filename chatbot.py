import os
from langchain_groq import ChatGroq

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",   # ✅ FIXED MODEL
    temperature=0.4
)

def get_chatbot_response(user_question):

    # safety check
    if not user_question or user_question.strip() == "":
        return "Please enter a valid question."

    prompt = f"""
You are an AI Health Assistant.
Give only general health advice.
Do not prescribe medicine.
Recommend doctor for serious cases.

User question: {user_question}
"""

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"
