import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


load_dotenv()                                           #load the env file

my_api_key = os.getenv("GROQ_API_KEY")                  #read the api key from the env file

if not my_api_key:
    raise ValueError("API key kaha hai bhai")


client = Groq(api_key=my_api_key)                       #connet to groq
model = "llama-3.3-70b-versatile"                       #select the ai model
role = "user"                                           #define the role


from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema = Ticket.model_json_schema()

response_format = {
    "type" : "json_object"
    }

system_prompt = f"""
Extract the information from the customer support ticket according to the following schema.
Return only a JSON object.
{schema}
"""

text = """My name is aryan jangid. I am from jaipur. I bought a iphone from your stor and which is not working at all.
       My email is abc@gmail.com. My mobile number is 1234567890"""

prompt = f"""This is a customer ticket. Please extract the personal information from this.
{text}
"""

message_system = {
    "role" : "system",
    "content" : system_prompt
    }

message = {
    "role":role,
    "content":prompt
    }

messages = [message_system,message]

response = client.chat.completions.create(model=model,messages=messages,response_format=response_format)

answer = response.choices[0].message.content
print(answer)





