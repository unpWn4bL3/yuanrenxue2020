import { readFileSync } from 'fs';

const wasmBuffer = readFileSync('encode.wasm');
const encode = await WebAssembly.instantiate(wasmBuffer).
    then(wasmModule => wasmModule.instance.exports["encode"]);

function getM() {
    let t1 = parseInt(Date.parse(new Date()) / 1000 / 2);
    let t2 = parseInt(Date.parse(new Date()) / 1000 / 2 - Math.floor(Math.random() * (50) + 1));
    let m = encode(t1, t2).toString() + '|' + t1 + '|' + t2;
    return m
}
// console.log(encode(848728123, 848728073));
console.log(getM());