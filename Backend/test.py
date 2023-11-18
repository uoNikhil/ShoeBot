from openai import OpenAI
from config import openAiKey
import json



text_to_analyze = "What is the difference between football studs and cleats"

def call_openai_api(text):
    client = OpenAI(api_key=openAiKey)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ]
        )
        print("--------------------------------------")
        print(response)
        print("--------------------------------------")
        # Accessing the first choice and its message
        choice = response.choices[0]
        message = choice.message

        # Extracting the content from the message
        if message.role == 'assistant':
            return message.content
        else:
            return "No response from the assistant."
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

def call_openai_api2(text):
    client = OpenAI(api_key=openAiKey)  # Replace with your actual API key

    try:
        response = client.chat.completions.create(
            model="text-davinci-003",  # Using a different model that might be more efficient
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ],
            max_tokens=150  # Limiting the number of tokens to speed up the response
        )
        
        # Accessing the first choice and its message
        choice = response.choices[0]
        message = choice.message

        # Extracting the content from the message
        if message.role == 'assistant':
            return message.content
        else:
            return "No response from the assistant."
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None


def call_openai_api3(text):
    client = OpenAI(api_key=openAiKey)  # Replace with your actual API key

    try:
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using the chat-compatible model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ],
            max_tokens=150,  # Limiting the number of tokens
            stream=True  # Enabling streaming of responses
        )

        for chunk in stream:
            if chunk['role'] == 'assistant':
                print(chunk['content'])

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")

############################################################################################################################

# Load your JSON data
with open('nike.json', 'r') as file:
    json_data = json.load(file)

# Example of how you might use the JSON data
# You need to format this according to your specific JSON structure
conversation_history = json_data.get("conversation_history", [])

# Add your instruction
conversation_history.append({"role": "system", "content": "You are a helpful assistant that suggests shoes to User"})

# Example user message
conversation_history.append({"role": "user", "content": "I'm looking for a new pair of running shoes"})

def call_openai_api4():
    client = OpenAI(api_key=openAiKey)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=150
        )

        for message in response.choices:
            if message['role'] == 'assistant':
                print(message['content'])

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")

call_openai_api()


resp = call_openai_api4(text_to_analyze)
print(resp)
