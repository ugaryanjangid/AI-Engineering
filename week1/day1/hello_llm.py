import os                             # Import os module to read environment variables            
from pathlib import Path
from dotenv import load_dotenv        # Import dotenv to load the .env file  
from groq import Groq                 # Import Groq library 

load_dotenv()         # Load the .env file

my_api_key = os.getenv("GROQ_API_KEY")               # Read the API key from the .env file

if not my_api_key:                                   # Check if API key exists
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key = my_api_key)                  # Connect to Groq using the API key

model = "llama-3.3-70b-versatile"                    # Select the AI model

role = "user"                                        # Role tells who is sending the message

prompt = "Do you know aryan jangid"                  # The question we want to ask

# Create one message
message = {
    "role" : role,
    "content" : prompt
}

messages=[message]                               # Put the message inside a list

   
# Send the message to the AI model
response = client.chat.completions.create(model=model, messages=messages )

print(response)                                       # Print the complete response

print(response.choices[0].message.content)            # Print only the AI's answer



#Load API Key → Connect to Groq → Choose Model → Write Prompt → Create Message → Send Request → Get Response → Print Answer