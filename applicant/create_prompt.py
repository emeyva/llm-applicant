from yaml import safe_load

def create_prompt(confige_file):
    application_form = ""
    with open(confige_file, 'r') as file:
        application_form = safe_load(file)

    user_name = application_form['applicant']['complete_name']
    user_bio = application_form['applicant']['applicant_bio']
    user_cv = application_form['applicant']['cv_content']
    app_info = application_form['applicant']['application_information']
    tokens = int(3000/4) # 3000 chars = one page

    # Design final prompt
    prompt = f"My name is {user_name} and here is a small bio of myself:\n{user_bio}\n\n"
    prompt += f"Here is some relevant information present on my CV:\n{user_cv}\n\n"
    prompt += f"I need you to write a Cover Letter, with around {tokens} tokens for the following job position:\n{app_info}\n\n"
    prompt += f"Make it formal, short and not too boring.\n"
    prompt += f"Before writing the Cover Letter, summarise the job opportunity and my Curriculum in two different set of bullet points"

    # 1 page = 500 words = 3000 chars
    # 1 token = 4 chars
    # 1 page = 3000/4 = 750 tokens
    return prompt