import os
from dotenv import load_dotenv 
from openai import OpenAI
import openai

load_dotenv()
# api_key = os.environ.get("OPENAI_API_KEY")
# print(f"API Key: {api_key}")  # In API Key ra để kiểm tra
# client = OpenAI(
#     api_key=os.environ.get("OPENAI_API_KEY")
# )


# # Tạo completion
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-3.5-turbo",  # Đảm bảo bạn sử dụng model hợp lệ, không phải "gpt-4o"
# )

# # In kết quả
# print(chat_completion.choices[0].message.content)
class GPT_Model:
    def output(input_text):
        client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),base_url="https://api.yescale.io/v1")
        response = client.chat.completions.create(model="gpt-4o-mini", messages = [
            {
                "role": "user",
                "content": input_text,
            }
        ])
        print(response.choices[0].message.content)

        return response.choices[0].message.content


