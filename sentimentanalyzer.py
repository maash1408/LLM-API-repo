"""
Groq API - Sentiment Analyzer
"""

from groq import Groq

client = Groq(
    api_key="",
)

def analyze_sentiment(text):
    """Analyze Sentiment of Text"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":"You are a Sentiment Analysis expert. Classify the sentiment as positive, negative or neutral. Provide aa confidence score"
            },
            {
                "role":"user",
                "content":f"Analyze the sentiment of {text}"
            }
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

reviews = [
    "This product is amazing! I love it!",
    "Terrible quality, waste of money.",
    "It's ok, nothing special."
]

for review in reviews:
    print(f"\nReview: {review}")
    print(f"Sentiment: {analyze_sentiment(review)}")
