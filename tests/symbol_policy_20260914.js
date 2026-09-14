function hasSymbol(value) {
  return /[^A-Za-z0-9]/.test(value);
}

console.assert(hasSymbol('Abc@123'));
console.assert(!hasSymbol('Abc123'));
console.assert(hasSymbol('pass-word'));
console.log('Symbol policy passed');
