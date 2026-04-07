"""
Groq API - Basic Usage
"""

from groq import Groq

client = Groq(
    api_key="",
)

conversation_history=[
    {
        "role":"system",
        "content":"You are a hepful AI Assistant"
    }
]

def chat(user_message):
    """Send message and get response"""

    conversation_history.append(
        {
            "role": "user",
            "content": user_message
        }
    )
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history,
        max_tokens=1000,
        temperature=0.7
    )
    assistant_message=response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    print(conversation_history)
    return assistant_message

print(chat("What is python"))
print(chat("I want to learn is Python, So please help me"))
