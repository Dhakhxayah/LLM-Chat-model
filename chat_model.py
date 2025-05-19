import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,  
)

messages = [
    SystemMessage(content = "Solve the following math problem"),
    HumanMessage(content = "What is 81 divided by 9")
]
response = model.invoke(messages)
print("Answer by AI:",response.content)
