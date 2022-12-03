# Встроенная функция
print(bin(int(input()))[2:])

# Алгоритмическое решение
n = int(input())
result = ''
while n > 0:
    result = str(n % 2) + result
    n //= 2
print(result)
