import os
from typing import Dict, List
from groq import Groq

# Get a free API key from https://console.groq.com/keys
# Set os.environ["GROQ_API_KEY"]

LLAMA3_70B_INSTRUCT = "llama3-70b-8192"
LLAMA3_8B_INSTRUCT = "llama3-8b-8192"

DEFAULT_MODEL = LLAMA3_70B_INSTRUCT
DEFAULT_OUTPUT = "output.txt"

client = Groq()

def write_output(response: str, output_file: str = DEFAULT_OUTPUT):
    with open(output_file, "w") as file:
            print(f"---\nSaving output to {output_file}")
            file.write(response)

def assistant(content: str):
    return { "role": "assistant", "content": content }

def user(content: str):
    return { "role": "user", "content": content }

def chat_completion(
    messages: List[Dict],
    model = DEFAULT_MODEL,
    temperature: float = 0.6,
    top_p: float = 0.9,
) -> str:
    response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        top_p=top_p,
    )
    return response.choices[0].message.content
        

def completion(
    prompt: str,
    model: str = DEFAULT_MODEL,
    temperature: float = 0.6,
    top_p: float = 0.9,
) -> str:
    return chat_completion(
        [user(prompt)],
        model=model,
        temperature=temperature,
        top_p=top_p,
    )

def complete_and_print(prompt: str, model: str = DEFAULT_MODEL, output_file: str = DEFAULT_OUTPUT):
    # print(f'==============\n{prompt}\n==============')
    response = completion(prompt, model)
    print(response, end='\n\n')
    write_output(response=response, output_file=output_file)

