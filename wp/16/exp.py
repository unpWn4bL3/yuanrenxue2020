import requests
import json
import subprocess
import httpx

client = httpx.Client(http2=True, verify=False)
api = "https://match.yuanrenxue.cn/api/match/16"
headers = {"User-Agent": "yuanrenxue.project"}
cookies = {"sessionid": "tdkjjaskxcf8dl0wr27o44n5q5zrsdg9"}
sum = 0

for i in range(1, 6):
    p = subprocess.Popen(["node", "./index.js"], stdout=subprocess.PIPE)
    jsons = p.stdout.read().decode("utf-8")
    data = json.loads(jsons)
    params = {"page": i, "m": data["m"], "t": data["t"]}
    print(params)
    r = client.get(api, params=params, headers=headers, cookies=cookies)
    for data in r.json()["data"]:
        sum += data["value"]
print(sum)
