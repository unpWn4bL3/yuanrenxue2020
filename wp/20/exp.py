import time
import requests
import hashlib

api = "https://match.yuanrenxue.cn/api/match/20"

# "1|1697270142000D#uqGdcw41pWeNXm"

sum = 0

for i in range(1, 6):
    timestamp = int(time.time() * 1000)
    signstr = str(i) + "|" + str(timestamp) + "D#uqGdcw41pWeNXm"
    hash = hashlib.md5()
    hash.update(signstr.encode())
    sign = hash.hexdigest()
    params = {"page": i, "sign": sign, "t": timestamp}
    headers = {"User-Agent": "yuanrenxue.project"}
    cookies = {
        "sessionid": "r2rdhnzu0fnenmstzj6fbhpllvlcukfz	",
    }
    r = requests.get(url=api, params=params, cookies=cookies, headers=headers)
    for d in r.json()["data"]:
        sum += d["value"]
    time.sleep(1)
print(sum)

"""
wasm在sign::md5几个方法前下断点，用getStringFromWasm0
去看内存，是标准md5(页数|时间戳salt)
"""
