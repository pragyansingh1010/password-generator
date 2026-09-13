def valid_length(length):
    return isinstance(length, int) and 8 <= length <= 64

assert valid_length(8)
assert valid_length(32)
assert valid_length(64)
assert not valid_length(7)
assert not valid_length(65)
print("Password length policy tests passed")
