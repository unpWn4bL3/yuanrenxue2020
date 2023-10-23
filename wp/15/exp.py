"""
window.m = function (){
            t1 = parseInt(Date.parse(new Date())/1000/2);
            t2 = parseInt(Date.parse(new Date())/1000/2 - Math.floor(Math.random() * (50) + 1));
            return window.q(t1, t2).toString() + '|' + t1 + '|' + t2;
        };
"""
import subprocess
import requests

cookies = {"sessionid": "tdkjjaskxcf8dl0wr27o44n5q5zrsdg9"}
headers = {"User-Agent": "yuanrenxue.project"}
api = "https://match.yuanrenxue.cn/api/match/15"

sum = 0
for i in range(1, 6):
    p = subprocess.Popen(["node", "./index.js"], stdout=subprocess.PIPE)
    m = p.stdout.read().decode("utf-8").rstrip()
    params = {"page": i, "m": m}
    r = requests.get(url=api, params=params, headers=headers, cookies=cookies)
    for d in r.json()["data"]:
        sum += d["value"]
print(sum)
