import './md5.js'

const r = {
    "page": 1,
    "m": "X7xxZE2CxYEHQBQ4bd221fabddb144ac27b786d7eb00eb3fJnjffMTpX",
    "t": 1697607931000 // timestamp
}

var window = global

const _0x34e7 = [
    "split",
    "ABHICESQWK",
    "FKByN",
    "U987654321",
    "lmHcG",
    "dICfr",
    "Szksx",
    "Bgrij",
    "iwnNJ",
    "jihgfdecba",
    "GfTek",
    "gfdecbaZXY",
    "constructo",
    "QIoXW",
    "jLRMs",
    "AqLWq",
    "0zyxwvutsr",
    "TKgNw",
    "eMnqD",
    "thjIz",
    "btoa",
    "MNPQRSTWXY",
    "oPsqh",
    "niIlq",
    "evetF",
    "LVZVH",
    "fYWEX",
    "kmnprstwxy",
    "aYkvo",
    "tsrqpomnlk",
    "HfLqY",
    "aQCDK",
    "lGBLj",
    "test",
    "3210zyxwvu",
    "QWK2Fi",
    "return /\" ",
    "hsJtK",
    "jdwcO",
    "SlFsj",
    "OWUOc",
    "LCaAn",
    "[^ ]+)+)+[",
    "FAVYf",
    "2Fi+987654",
    "floor",
    "join",
    "EuwBW",
    "OXYrZ",
    "charCodeAt",
    "SkkHG",
    "iYuJr",
    "GwoYF",
    "kPdGe",
    "cVCcp",
    "INQRH",
    "INVALID_CH",
    "f.charAt",
    "push",
    "apply",
    "lalCJ",
    "kTcRS",
    "+ this + \"",
    "ykpOn",
    "gLnjm",
    "gmBaq",
    "kukBH",
    "dvEWE",
    "SFKLi",
    "^([^ ]+( +",
    "qpomnlkjih",
    "^ ]}",
    "pHtmC",
    "length"
]

const u = function (e) {
    return _0x34e7[e -= 188]
}

function d(e) {
    var t = u
        , n = {};
    n[t(214)] = function (e, t) {
        return e || t
    }
        ,
        n.bWcgB = function (e, t) {
            return e * t
        }
        ,
        n[t(227)] = "ABCDEFGHJK" + t(209) + "Zabcdefhij" + t(215) + "z2345678";
    for (var r = n, o = "1|3|0|4|2|5"[t(188)]("|"), a = 0; ;) {
        switch (o[a++]) {
            case "0":
                var s = l[t(261)];
                continue;
            case "1":
                e = r[t(214)](e, 32);
                continue;
            case "2":
                for (let i = 0; i < e; i++)
                    c += l['charAt'](Math[t(233)](r.bWcgB(Math.random(), s)));
                continue;
            case "3":
                var l = r[t(227)];
                continue;
            case "4":
                var c = "";
                continue;
            case "5":
                return c
        }
        break
    }
}

const sign = function (e) {
    var t = u
        , r = {};
    let f = "U9876543210zyxwvutsrqpomnlkjihgfdecbaZXYWVUTSRQPONABHICESQWK2Fi+9876543210zyxwvutsrqpomnlkjihgfdecbaZXYWVUTSRQPONABHICESQWK2Fi";
    r.TGmSp = "INVALID_CHARACTER_ERR",
        r['SkkHG'] = 'return /" + this + "/',
        r[t(205)] = '^([^ ]+( +[^ ]+)+)+[^ ]}',
        r.aYkvo = function (e) {
            return e()
        }
        ,
        r[t(254)] = function (e, t) {
            return e % t
        }
        ,
        r.evetF = function (e, t) {
            return e >> t
        }
        ,
        r.GfTek = t(196),
        r[t(260)] = function (e, t) {
            return e << t
        }
        ,
        r[t(229)] = function (e, t) {
            return e | t
        }
        ,
        r[t(242)] = function (e, t) {
            return e << t
        }
        ,
        r[t(228)] = function (e, t) {
            return e & t
        }
        ,
        r[t(207)] = function (e, t) {
            return e << t
        }
        ,
        r[t(202)] = function (e, t) {
            return e & t
        }
        ,
        r.jdwcO = function (e, t) {
            return e === t
        }
        ,
        r.kPdGe = t(231),
        r[t(195)] = t(213),
        r[t(201)] = function (e, t) {
            return e & t
        }
        ,
        r[t(206)] = function (e, t) {
            return e == t
        }
        ,
        r[t(219)] = function (e, t) {
            return e + t
        }
        ,
        r[t(220)] = function (e, t) {
            return e(t)
        }
        ;
    var i = r;
    for (var o, a, s, l = 0, c = []; l < e.length;) {
        switch (a = e.charCodeAt(l), s = l % 6) {
            case 0:
                c.push(f.charAt(i[t(212)](a, 2)));
                break;
            case 1:
                try {
                    c.push(f.charAt(i.pHtmC(2 & o, 3) | i.evetF(a, 4)))
                } catch (e) {
                    c.push(f.charAt(i[t(229)](i.cVCcp(3 & o, 4), a >> 4)))
                }
                break;
            case 2:
                c.push(f.charAt(i[t(229)](i[t(242)](15 & o, 2), i.evetF(a, 6)))),
                    c.push(f.charAt(i[t(228)](a, 63)));
                break;
            case 3:
                c.push(f.charAt(i[t(212)](a, 3)));
                break;
            case 4:
                c.push(f.charAt(i[t(229)](i[t(207)](i.OWUOc(o, 4), 6), i[t(212)](a, 6))));
                break;
            case 5:
                c.push(f.charAt(i[t(229)](i[t(207)](i[t(202)](o, 15), 4), a >> 8))),
                    c.push(f.charAt(i[t(202)](a, 63)))
        }
        o = a,
            l++
    }
    // console.log(e, c.join("") + "UFM", window.md5(c.join("") + "UFM"))
    return d(15) + window.md5(c.join("") + "UFM") + d(10)
}

const getm = () => {
    const t = Date.parse(new Date).toString()
    const m = sign(`${t}`)
    return JSON.stringify({
        t,
        m
    })
}
// sign('1697617257000')
console.log(getm())

// y7nQ4eNxrdO4UUOy    y7nQ4eNxr6N4UOy
// y7nQ4eNxrdO4UUOyUFM y7nQ4eNxr6N4UOyUFM

// 1697617257000 y7nQ4eNxr2I4UOyUFM 95a153498a8f59733fb3baf67c85bacc
// 1697617257000 y7nQ4eNxr2I4UOyUFM 95a153498a8f59733fb3baf67c85bacc