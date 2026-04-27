from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOllama(model="llama3", temperature=0.4)

def get_chatbot_response(user_question):

    messages = [
        SystemMessage(content="""
You are an AI Health Assistant.
Give only general health advice.
Do not prescribe medicine.
Advise doctor for emergencies.
"""),

        HumanMessage(content=user_question)
    ]

    response = llm.invoke(messages)

    return response.content