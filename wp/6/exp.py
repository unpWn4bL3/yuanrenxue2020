import json
import time
import requests
import subprocess

api = "https://match.yuanrenxue.cn/api/match/6"

sum = 0

for i in range(1, 6):
    p = subprocess.Popen(["node", "./exp.js"], stdout=subprocess.PIPE)
    data = p.stdout.read().decode("utf-8")
    params = json.loads(data)
    params["page"] = i
    r = requests.get(api, params)
    values = r.json()
    for v in values["data"]:
        sum += v["value"] * 24
    time.sleep(1.0)

print(sum)
