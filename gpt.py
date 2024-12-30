import os
from dotenv import load_dotenv 
from openai import OpenAI


load_dotenv()
# api_key = os.environ.get("OPENAI_API_KEY")
# print(f"API Key: {api_key}")  # In API Key ra để kiểm tra
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


# Tạo completion
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",  # Đảm bảo bạn sử dụng model hợp lệ, không phải "gpt-4o"
)

# In kết quả
print(chat_completion.choices[0].message.content)