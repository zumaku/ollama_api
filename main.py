# Source:
# https://github.com/ollama/ollama-python

import ollama

response = ollama.chat(
    model='llama3',
    messages=[{
        'role': 'user',
        'content': 'Tell me a joke?',
    }],
    stream=True,
)

for chunk in response:
  print(chunk['message']['content'], end='', flush=True)