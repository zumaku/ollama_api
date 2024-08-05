# Source:
# https://pypi.org/project/ollama/
# Pada bagian Costum client
# ---------------------------------------
# Gunakan juga struktur stream di sini:
# https://github.com/ollama/ollama-python

from ollama import Client
client = Client(host='http://localhost:11434')
stream = client.chat(
  model='tinyllama',
  messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
  ],
  stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)