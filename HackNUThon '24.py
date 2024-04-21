import os

from groq import Groq

client = Groq(
    api_key='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'
)
user=input("Enter your query: ")
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user,
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)