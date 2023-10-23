import re
import requests

url = "https://match.yuanrenxue.cn/match/13"
api = "https://match.yuanrenxue.cn/api/match/13"

s = requests.session()
s.cookies.set("sessionid", "qk5lwvxnr14315tr92iw95rczihr9k44")  # 在一开始就要传入登陆的sessionid
r = s.get(url)
match = re.match(r"<script>document\.(.*)\+';path=\/'", r.text)
code = match.group(1).lstrip().replace("cookie=", "")
yuanrenxue_cookie = eval(code).replace("yuanrenxue_cookie=", "")
s.cookies.set("yuanrenxue_cookie", yuanrenxue_cookie)
headers = {"User-Agent": "yuanrenxue.project"}

sum = 0
for i in range(1, 6):
    params = {"page": i}
    r = s.get(api, params=params, headers=headers, cookies=s.cookies)
    for d in r.json()["data"]:
        sum += d["value"]

print(sum)
