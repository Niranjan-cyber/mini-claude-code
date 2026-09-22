import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
    api_key=os.getenv("GROQ_API_KEY"),
)

messages = []

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ('exit', 'quit', 'bye'):
        print("AI: Bye! Have a great day.")
        break
    
    messages.append({"role": "user", "content" : user_input})

    response = client.chat.completions.create(
        model = "openai/gpt-oss-120b",
        messages = messages,
    )
    
    ai_response = response.choices[0].message.content
    print("AI:", ai_response)
    
    messages.append({"role": "assistant", "content": ai_response})
    