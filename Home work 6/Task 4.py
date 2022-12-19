lst = [int(x) for x in input().split()]
print([x * y for x, y in zip(lst[:len(lst) // 2 + len(lst) % 2], lst[::-1])])
