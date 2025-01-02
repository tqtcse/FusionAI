import os
import anthropic
from dotenv import load_dotenv 
from IPython.display import Markdown, display
from anthropic import HUMAN_PROMPT, AI_PROMPT

load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")
print(f"API Key: {api_key}")  # In API Key ra để kiểm tra

client = anthropic.Anthropic(
	api_key = os.environ["ANTHROPIC_API_KEY"], 
)

completion = client.completions.create(
    model="claude-2.1",
    max_tokens_to_sample=300,
    prompt=f"{HUMAN_PROMPT} What is Matthew effect? {AI_PROMPT}",
)
Markdown(completion.completion)

