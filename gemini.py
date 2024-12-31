import os
import google.generativeai as genai 
from dotenv import load_dotenv 

load_dotenv()

# api_key = os.environ.get("GEMINI_API_KEY")
# print(f"API Key: {api_key}")  # In API Key ra để kiểm tra

genai.configure(api_key = os.environ["GEMINI_API_KEY"], )

# model = genai.GenerativeModel('gemini-1.5-flash')

def output(input_text):
	model = genai.GenerativeModel("gemini-1.5-flash")
	response = model.generate_content(input_text)
	print(response.text)

# output('hello')


if __name__ == "__main__":
    while True:
        user_input = input("Enter your prompt (or type 'exit' to quit): ")
        if user_input.lower() == "exit":  # Kiểm tra điều kiện thoát
            print("Exiting the program. Goodbye!")
            break
        output(user_input)