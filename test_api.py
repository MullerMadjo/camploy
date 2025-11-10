import requests

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": "Bearer sk-87af864002e94fc8b1a585f9d3df3129",
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Bonjour, est-ce que ma clé fonctionne ?"}
    ],
    "stream": False
}

resp = requests.post(url, headers=headers, json=data)

print("Status code:", resp.status_code)
print("Response:", resp.text)
