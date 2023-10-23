import requests
import base64

api = "https://match.yuanrenxue.cn/api/match/12"
sum = 0
headers = {"User-Agent": "yuanrenxue.project"}
cookies = {"sessionid": "r2rdhnzu0fnenmstzj6fbhpllvlcukfz"}
for i in range(1, 6):
    params = {"page": i, "m": base64.b64encode(f"yuanrenxue{i}".encode())}
    r = requests.get(api, params, cookies=cookies, headers=headers)
    for d in r.json()["data"]:
        sum += d["value"]
print(sum)
