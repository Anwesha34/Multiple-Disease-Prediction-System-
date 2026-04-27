from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatGroq(
    api_key="YOUR_GROQ_API_KEY",
    model="llama3-8b-8192",
    temperature=0.4
)

def get_chatbot_response(user_question):

    messages = [
        SystemMessage(content="""
You are an AI Health Assistant.
Give only general health advice.
Do not prescribe medicine.
Recommend doctors for serious cases.
"""),
        HumanMessage(content=user_question)
    ]

    response = llm.invoke(messages)
    return response.content
