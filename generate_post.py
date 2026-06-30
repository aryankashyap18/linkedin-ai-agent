from google import genai
import os
from datetime import datetime

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
Write a professional LinkedIn post about AI Automation or Business Automation.

Rules:
- Strong first line
- 150-250 words
- Practical and engaging
- End with a question
- Add 5 relevant hashtags
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

post = response.text

today = datetime.now().strftime("%Y-%m-%d")

os.makedirs("posts", exist_ok=True)

with open(f"posts/{today}.md", "w", encoding="utf-8") as f:
    f.write(post)

print(post)
