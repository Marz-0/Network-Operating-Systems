import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
updated_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "This post content has been updated.",
    "userId": 1
}

response = requests.put(url, json=updated_data)
print(f"Status Code: {response.status_code}")
print("Updated Resource:", response.json())
