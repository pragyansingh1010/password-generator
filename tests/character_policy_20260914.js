function hasRequiredTypes(value) {
  return /[a-z]/.test(value) && /[A-Z]/.test(value) && /\d/.test(value);
}

console.assert(hasRequiredTypes('Abc123'));
console.assert(!hasRequiredTypes('abcdef'));
console.assert(!hasRequiredTypes('ABCDEF'));
console.log('Character policy passed');
