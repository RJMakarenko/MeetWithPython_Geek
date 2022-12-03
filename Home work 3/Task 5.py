# Не нравится мне этот алгоритм, но как придумал...

fibonacci = [0, 1]
n = int(input())
for i in range(2, n):
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
negafibonacci = fibonacci[:]
for i in range(1, len(fibonacci)):
    item = fibonacci[i] if i % 2 != 0 else -fibonacci[i]
    negafibonacci.insert(0, item)
print(negafibonacci)
