# Import os module to read environment variables
import os 

# Import dotenv to load the .env file                      
from pathlib import Path

# Import Groq library
from dotenv import load_dotenv

# Import Groq library
from groq import Groq

# Load the .env file
load_dotenv()

# Read the API key from the .env file
my_api_key = os.getenv("GROQ_API_KEY")

# Check if API key exists
if not my_api_key:
    raise ValueError("API key kaha hai bhai")

# Connect to Groq using the API key
client = Groq(api_key = my_api_key)

# Select the AI model
model = "llama-3.3-70b-versatile"

# Role tells who is sending the message
role = "user"

# The question we want to ask
prompt = "Suggest me a name for my cloth brand"

#SYSTEM
message_system = {
    "role" : "system",
    "content" : "You are a brand manager who suggest a name for my brand .suggest me a name in a one word"
}

# Create one message
message = {
    "role" : role,
    "content" : prompt
}

# Put the message inside a list
messages=[message_system, message]
   
#Temprature by default is 0  - meaning safe  range is [0,2]
# Send the message to the AI model
response = client.chat.completions.create(model=model, messages=messages, temperature=0 )

# Print the complete response
# print(response)

print("########################################")

# Print only the AI's answer
print(response.choices[0].message.content)

