import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()
print(json.dumps(data,indent=4))