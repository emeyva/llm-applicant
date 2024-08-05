# LLM-Applicant
A Python CLI that leverages llms capabilities to create specific cover letters

## Plan
Started as a playgroung project to learn more about promp-engineering.

A job application usually requests a cover letter.
This usually is a type of motivation letter that shows how your skills overlap with the ones from the job requisites.
Some of these skills are present on CVs, our bios, or other forms.

Can we use a Large Language Model to help us write a draft Cover Letter?

Let's prompt engineer Llama3 model to output a tailored Cover Letter!

## Run it!
Set config.yaml with your own data
| Values |
| ------ |
| application_information   |
| applicant_bio | 
| cv_content    |
| complete_name    |

Set your GROQ_API_KEY
```console
foo@bar:~$ export GROQ_API_KEY=<YOUR_API_KEY>
```
Get a free API key [here](https://console.groq.com/keys)

Just run run_applicant.py

```console
foo@bar:~$ python3 run_applicant.py
**Job Opportunity Summary:**
...
**Your Curriculum Summary:**
...
Now, I'll write a Cover Letter tailored to the job opportunity:
...
```

## Models

Using groq client
- llama3-70b-8192 (default)
- llama3-8b-8192

## References

Prompt Engineering with Llama 3 - [llama-recipes](https://github.com/meta-llama/llama-recipes/blob/main/recipes/quickstart/Prompt_Engineering_with_Llama_3.ipynb)