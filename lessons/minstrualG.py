MISTRAL_API_KEY = 'WPBZaq7lrqbzjOPXFL2f8BFWLprRkhAx'
from mistralai import Mistral
import base64


model = "mistral-large-latest"

client = Mistral(api_key=MISTRAL_API_KEY)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is a menstrual cycle?",
        },
    ]
)

print(chat_response.choices[0].message.content)