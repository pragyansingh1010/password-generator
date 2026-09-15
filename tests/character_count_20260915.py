def has_min_length(password, minimum):
    return len(password) >= minimum

assert has_min_length('abcdef', 6)
assert not has_min_length('abc', 6)
