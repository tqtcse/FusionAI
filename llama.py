import os
from dotenv import load_dotenv
from groq import Groq

# api_key = os.environ.get("GROQ_API_KEY")
# print(f"API Key: {api_key}")  # In API Key ra để kiểm tra

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
class Llama_Model:
	def output(user_input):
		chat_completion = client.chat.completions.create(
	    messages=[
	        {
	            "role": "user",
	            "content": user_input,
	        }
	    ],
	    model="llama-3.3-70b-versatile",
		)

		print(chat_completion.choices[0].message.content)
		return chat_completion.choices[0].message.content
