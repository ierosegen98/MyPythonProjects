n = int(input())  
k = int(input("Введите основание новой системы счисления: "))
result = ''

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n > 0:
    digit = n % k
    result = digits[digit] + result
    n //= k

print(result)