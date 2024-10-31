import requests

url = "https://api.webflow.com/v2/collections/collection_id/items"

payload = {
    "isArchived": False,
    "isDraft": False,
    "fieldData": { "newKey": "New Value" }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)