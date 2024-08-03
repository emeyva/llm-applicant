# llm-applicant
a python cli that leverages llms capabilities to create specific cover letters

## plan

So a job application evolves usually writing a cover letter.
This usually is motivation letter that infuses some of your skills, some are present on your CV, some are not.

Can we use a Large Language Model to help us write this Cover Letter with our info in context?


## configuration
Set applicant/config.yaml with your own data
| Values |
| ------ |
| application_information   |
| applicant_bio | 
| cv_content    |

Set your GROQ_API_KEY
```console
foo@bar:~$ export GROQ_API_KEY=<YOUR_API_KEY>
```
Get a free API key [here](https://console.groq.com/keys)

Just run run_applicant.py

```console
foo@bar:~$ python3 run_applicant.py
--- Your Cover Letter ---
Here is a cover letter tailored to the ...
```

## model

Using llama3-70b-8192 through groq client