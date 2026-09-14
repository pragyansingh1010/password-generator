function hasUppercase(value) {
  return /[A-Z]/.test(value);
}

console.assert(hasUppercase('Abc123'));
console.assert(hasUppercase('ABC'));
console.assert(!hasUppercase('abc123'));
console.log('Uppercase policy passed');
