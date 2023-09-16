def factorial(num):
    if num == 1:
        result = num
        return result
    else:
        result = factorial(num-1) * num
        return result
num = int(input('введите число'))
print(factorial(num))