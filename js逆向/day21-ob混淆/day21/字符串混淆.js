const code = `
var a = 'hello world'
`;
const options = {
  compact: false,
  unicodeEscapeSequence: true  //对字符串进行 Unicode 转码
};

const obfuscator = require('javascript-obfuscator')

function obfuscate(code, options) {
  return obfuscator.obfuscate(code, options).getObfuscatedCode()
}

console.log(obfuscate(code, options))
