def multiplier(n, m):
    if m == 1:
        return n
    return n + multiplier(n, m-1)

print(multiplier(5, 3))
print(multiplier(6, 6))
print(multiplier(9, 7))