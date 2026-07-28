# Import os module to read environment variables
import os

# Import Path module (currently not used in this code)
from pathlib import Path

# Import load_dotenv to load the .env file
from dotenv import load_dotenv

# Import Groq library to connect with the Groq AI model
from groq import Groq


# Load the .env file
load_dotenv()

# Read the API key from the .env file
my_api_key = os.getenv("GROQ_API_KEY")

# Check if the API key exists
if not my_api_key:
    raise ValueError("API key kaha hai bhai")

# Create a connection with the Groq AI using the API key
client = Groq(api_key=my_api_key)

# Select the AI model
model = "llama-3.3-70b-versatile"

# Define the role of the sender
role = "user"

# User's question (Prompt)
prompt = "Suggest me a name for my cloth brand"

# System Role:
# Tells the AI how to behave and what instructions to follow
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests a brand name. Suggest only one-word names."
}

# User message:
# Contains the user's prompt
message = {
    "role": role,
    "content": prompt
}

# Store both the system message and user message in a list
messages = [message_system, message]

# Temperature controls the creativity of the AI.
# 0 = Less creative, more accurate
# Range = 0 to 2
response = client.chat.completions.create(model=model,messages=messages,temperature=0)

# Print a separator line
print("########################################")

# Print only the AI's answer
print(response.choices[0].message.content)