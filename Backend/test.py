from openai import OpenAI
from config import openAiKey

text_to_analyze = "What is the difference between football studs and cleats"

def call_openai_api(text):
    client = OpenAI(api_key=openAiKey)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ],
            stream = True
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


resp = call_openai_api(text_to_analyze)
print(resp)
