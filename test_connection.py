import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API credentials
load_dotenv()

# Initialise OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Test the connection
response = client.responses.create(
    model="gpt-4o-mini",
    input="Say hello in one short sentence."
)

print(response.output_text)
