import initCycleTLS from 'cycletls';

const run = async (page) => {
    const cycleTLS = await initCycleTLS();
    const response = await cycleTLS(`https://match.yuanrenxue.cn/api/match/19?page=${page}`, {
        body: '',
        // chrome指纹去掉65037
        ja3: '771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,23-0-27-65281-51-43-18-45-10-35-13-17513-11-5-16,29-23-24,0',
        userAgent: 'yuanrenxue.project',
        cookies: {
            'sessionid': 'jaxr2aun6gdb7acec0u73o5qr74wxv51',
        }
    }, 'get')
    cycleTLS.exit()
    return response.body["data"]
}

let sum = 0
for (let i = 1; i < 6; i++) {
    const data = await run(i)
    data.forEach(element => {
        sum += element["value"]
    });
}
console.log(sum)