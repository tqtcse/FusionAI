import os
import google.generativeai as genai 
from dotenv import load_dotenv 

load_dotenv()

# api_key = os.environ.get("GEMINI_API_KEY")
# print(f"API Key: {api_key}")  # In API Key ra để kiểm tra

genai.configure(api_key = os.environ["GEMINI_API_KEY"], )

# model = genai.GenerativeModel('gemini-1.5-flash')

class Gemini_Model:
	def output(input_text):
		model = genai.GenerativeModel("gemini-1.5-flash")
		response = model.generate_content(input_text)
		print(response.text)

# output('hello')


