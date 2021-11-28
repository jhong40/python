import requests
endpoint = "https://slack.com/api/chat.postMessage"
data = {"channel":"Cxxxx", "text": "123 great goose turkey....blah blah ....test from python"}
headers = {"Authorization": "Bearer xoxb-xxxx"}
print(requests.post(endpoint, data=data, headers=headers).json())
