import requests
endpoint = "https://slack.com/api/chat.postMessage"
data = {"channel":"C02P5C5FCBT", "text": "123 great goose turkey....blah blah ....test from python"}
headers = {"Authorization": "Bearer xoxb-767624982948-2771827764917-1uLpXFx37dCU2A3yrsthDRNa"}
print(requests.post(endpoint, data=data, headers=headers).json())
