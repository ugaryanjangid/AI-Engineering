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
prompt = "Do you know aryan jangid"

# Create one message
message = {
    "role" : role,
    "content" : prompt
}

# Put the message inside a list
messages=[message]
   
# Send the message to the AI model
response = client.chat.completions.create(model=model, messages=messages )

# Print the complete response
print(response)

# Print only the AI's answer
print(response.choices[0].message.content)

#Load API Key → Connect to Groq → Choose Model → Write Prompt → Create Message → Send Request → Get Response → Print Answer