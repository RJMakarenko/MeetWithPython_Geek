# Проверка простоты числа
def simple(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# Разложение на простые множители (факторизация)
def factorization(number):
    result = []
    for i in range(int(number**0.5) * 2, 1, -1):
        if simple(i):
            if number % i == 0:
                while number % i == 0:
                    result.append(i)
                    number //= i
    return result


n = int(input('Введите число N: '))
print(factorization(n))
