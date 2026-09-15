def has_symbol(password):
    return any(not ch.isalnum() for ch in password)

assert has_symbol('abc!123')
assert not has_symbol('abc123')
