import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,  
)

chat_history = []

while True:
    query = input("You :")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content = response))
    print("Answer by AI:",response)

print("--------Message History---------")
for msg in chat_history:
    role = "You" if isinstance(msg, HumanMessage) else "AI"
    print(f"{role}: {msg.content}")

