import { parseScript } from 'esprima'
import { generate } from 'escodegen'
import { replace } from 'estraverse'
import { readFileSync } from 'fs'

const sourceCode = readFileSync('./m.js', { encoding: 'utf8' });
let ast = parseScript(sourceCode)

function hebing(ast) {
    replace(ast, {
        leave: function (node) {
            if (node.type === 'BinaryExpression' && node.operator === '+') {
                let left = node.left
                let right = node.right
                if (left.type === 'Literal' && right.type === 'Literal') {
                    return {
                        type: "Literal",
                        value: left.value + right.value
                    }
                }
            }
        }
    })
    return ast
}

function quluanma(ast) {
    replace(ast, {
        leave: function (node) {
            if (node.type === 'Literal') {
                return {
                    ...node,
                    value: node.value
                }
            }
        }
    })
    return ast
}

const newCode = generate(hebing(quluanma(ast)))
console.log(newCode)