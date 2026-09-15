def has_uppercase(password):
    return any(ch.isupper() for ch in password)

assert has_uppercase('Abc123')
assert not has_uppercase('abc123')
