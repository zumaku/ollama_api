# Artikel dari
# https://dev.to/jayantaadhikary/using-the-ollama-api-to-run-llms-and-generate-responses-locally-18b7

import requests
import json

url = "http://localhost:11434/api/generate"

header = {
    "Content-Type": "application/json"
}

data = {
    "model": "llama3",
    "prompt": "Why is the sky blue?",
    "stream": False
}

# response = requests.post(url, headers=header, data=json.dumps(data))
response = requests.post(url, headers=header, json=data)

if response.status_code == 200:
    response_text = response.text
    data = json.loads(response_text)
    actual_response = data["response"]
    print(actual_response)
else:
    print("Error:", response.status_code, response.text)