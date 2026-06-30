from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("prompt.txt", "r") as file:
    prompt = file.read()

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)
