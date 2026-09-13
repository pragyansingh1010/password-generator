def valid_count(value):
    return isinstance(value, int) and 1 <= value <= 64

assert valid_count(1)
assert valid_count(64)
assert not valid_count(0)
assert not valid_count(65)
print('Password character count rules passed')
