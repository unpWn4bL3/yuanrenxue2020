import httpx

api = "https://match.yuanrenxue.cn/api/match/19"
cookies = {"sessionid": "qk5lwvxnr14315tr92iw95rczihr9k44"}
headers = {"User-Agent": "yuanrenxue.project"}
client = httpx.Client(http2=True, verify=False)

sum = 0
for i in range(1, 6):
    params = {"page": i}
    r = client.get(api, params=params, cookies=cookies, headers=headers)
    for d in r.json()["data"]:
        sum += d["value"]
print(sum)
