
import openai
client = openai.OpenAI(api_key="sk-ExhRdk4XxObsRt2yht939zhKdONR9dW6pQUPG05OJ3drL8aQ",base_url="https://api.yescale.io/v1")
response = client.chat.completions.create(model="gpt-4o-mini", messages = [
    {
        "role": "user",
        "content": "Who is Lionel Messi?"
    }
])
print(response)