import base64
import io
import requests
from fontTools.ttLib import TTFont
import xml.etree.ElementTree as ET

api = "https://match.yuanrenxue.cn/api/match/7"

ons_to_num = {
    "1010010010010": "0",
    "10101010110101000101010110101010": "8",
    "10010101001110101011010101010": "9",
    "1010101010000101011101010110": "6",
    "11111111111": "4",
    "1111111": "7",
    "1110101001001010110101010100101011111": "5",
    "100110101001010101011110101000": "2",
    "10101100101000111100010101011010100101010100": "3",
    "1001101111": "1",
}

hex_to_num = {}
max = 0
idx = 1
maxidx = 0
for i in range(1, 6):
    params = {"page": i}
    r = requests.get(api, params)
    j = r.json()
    woff_str = j["woff"]
    data = j["data"]
    font = TTFont(io.BytesIO(base64.b64decode(woff_str)))
    font.saveXML("temp.xml")
    f = open("temp.xml")
    et = ET.parse(f)
    f.close()
    TTGlyphs = et.getroot().find("glyf").findall("TTGlyph")
    for TTGlyph in TTGlyphs:
        ons = ""
        hex = TTGlyph.attrib["name"].replace("uni", "")
        if ".notdef" in hex:
            continue
        for pt in TTGlyph.find("contour").findall("pt"):
            on = pt.attrib["on"]
            ons += on
        hex_to_num[hex] = ons_to_num[ons]

    for d in data:
        score = ""
        hexs = d["value"].replace("&#x", "").split()
        for hex in hexs:
            score += hex_to_num[hex]
        score = int(score)
        print(score)
        if max < score:
            max = score
            maxidx = idx
        idx += 1
    print("---")

print(max, maxidx)  # js里面name数组的idx
