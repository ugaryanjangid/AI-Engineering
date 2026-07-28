import os
from dotenv import load_dotenv
from groq import Groq

# Load the .env file
load_dotenv()

# Read the API key from the .env file
my_api_key = os.getenv("GROQ_API_KEY")

# Check if the API key exists
if not my_api_key:
    raise ValueError("API key kaha hai bhai")

# Connect to Groq
client = Groq(api_key=my_api_key)

# Select the AI model
model = "llama-3.3-70b-versatile"

# Define the role
role = "user"

# Create 3 prompts
prompt1 = "Hi!"
prompt2 = "Explain time travel in detail but under 100 words."
prompt3 = "Write a 1000-word essay on Machine Learning."

# Store all prompts in a list
prompts = [prompt1, prompt2, prompt3]

# Run the loop for each prompt
for prompt in prompts:

    # Create a user message
    message = {
        "role": role,
        "content": prompt
    }

    # Store the message inside a list
    messages = [message]

    # Send the request to the AI
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=5000
    )

    # Get token usage information
    usage = response.usage

    # Print the token details
    print(
        f"Prompt: {prompt}\n"
        f"Prompt Tokens: {usage.prompt_tokens}\n"
        f"Completion Tokens: {usage.completion_tokens}\n"
        f"Total Tokens: {usage.total_tokens}\n"
        f"Finish Reason: {response.choices[0].finish_reason}\n"
    )