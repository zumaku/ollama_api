import requests
import json

def fetch_streaming_response():
    url = "http://127.0.0.1:8000/chat/llama3"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3",
        "prompt": "Why is the sky blue?"
    }

    try:
        # Mengirimkan permintaan POST dengan streaming diaktifkan
        with requests.post(url, headers=headers, json=payload, stream=True) as response:
            response.raise_for_status()  # Akan menaikkan exception untuk status code 4xx/5xx
            
            # Menampilkan respons secara streaming
            for chunk in response.iter_lines():
                if chunk:
                    print(chunk.decode('utf-8'))

    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    fetch_streaming_response()
