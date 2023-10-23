import re
import subprocess
import requests

api = "https://match.yuanrenxue.cn/api/match/9"
cookies = {"sessionid": "hzgtko31jupvo1urf4g8ugpsjq376pkd"}
headers = {"User-Agent": "yuanrenxue.project"}

s = requests.session()
s.cookies.set("sessionid", "hzgtko31jupvo1urf4g8ugpsjq376pkd")
s.headers = headers

# 拿到动态的时间戳
r = s.get("https://match.yuanrenxue.cn/match/9")
pattern = re.compile("\(decrypt,\\'(\d*)\\'\)")  # (decrypt,\'1698074629\')
timestamp = pattern.search(r.text).group(1)

p = subprocess.Popen(["node", "udc.js", timestamp], stdout=subprocess.PIPE)
m = p.stdout.read().decode()[:-1]
cookies["m"] = m
sum = 0

for i in range(1, 6):
    params = {"page": i}
    r = s.get(api, params=params, headers=headers, cookies=cookies)
    for data in r.json()["data"]:
        sum += data["value"]
print(sum // 50)
