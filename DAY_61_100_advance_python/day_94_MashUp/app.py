# import requests, json, os
# import openai

# openai.organization = os.environ['organizationID']
# openai.api_key = os.environ['openai']
# openai.Model.list()

# prompt = "Who is the most handsome bald man?"

# response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=6)

# print(response["choices"][0]["text"].strip())