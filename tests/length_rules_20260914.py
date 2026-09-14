def valid_length(n):
    return isinstance(n, int) and n >= 1

assert valid_length(1)
assert valid_length(16)
assert not valid_length(0)
assert not valid_length(-2)
print('Password length rules passed')
