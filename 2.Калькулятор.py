a=int(input('Введите превое число'))
b=int(input('Введите второе число'))
operation=str(input('Введите операцию'))
if operation == '+':
    print(a+b)
elif operation == '-':
    print(a-b)
elif operation == '/':
    print(a/b)
elif operation == '*':
    print(a*b)
elif operation == 'mod':
    print(a%b)
elif operation == 'pow':
    print(a**b)
elif operation == 'div':
    print(int(a/b))