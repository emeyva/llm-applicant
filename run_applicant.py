from applicant.groq_client import chat_completion, user, assistant, complete_and_print, completion
from yaml import safe_load

CONFIG_FILE = "applicant/config.yaml"

if __name__ == '__main__':
    application_form = ""
    with open(CONFIG_FILE, 'r') as file:
        application_form = safe_load(file)

    prompt = f"Here is a small bio of myself: {application_form['applicant']['application_information']}\n"

    prompt += f"Here is some relvant information present on my CV: {application_form['applicant']['applicant_bio']}\n"

    prompt += f"I need you to write a Cover Letter for the following job position: {application_form['applicant']['application_information']}\n"

    prompt += f"Make it formal, short and not too boring"

    response = completion(prompt)

    print(f"--- Your Cover Letter ---\n\n{response}")


