from applicant.groq_client import complete_and_print
from applicant.create_prompt import create_prompt

CONFIG_FILE = "config.yaml"
OUTPUT_FILE = "output.txt"

def run_applicant():
    prompt = create_prompt(CONFIG_FILE)
    complete_and_print(prompt)

if __name__ == '__main__':
    run_applicant()
    