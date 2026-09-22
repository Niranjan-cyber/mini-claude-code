import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize client
client = OpenAI(
    base_url=os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
    api_key=os.getenv("GROQ_API_KEY"),
)

# Create a chat completion -> generate a response
# LLM only generates text  
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role":"system", "content": "You are a helpful AI Assistant. Answer concisely in few sentences"},
        {"role": "user", "content": "Explain what an AI Agent is in one sentence."},
        {"role": "assistant", "content": "An AI Agent is simply an LLM connected to tools in a loop"}],
)

print(response.choices[0].message.content)   