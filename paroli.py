import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

def parametrs():
    chars = ''
    lenght = int(input('Укажите длину одного пароля'))

    if input('Включать ли цифры 0123456789? (да/нет): ').lower() in ['да', 'д', 'yes']:
        chars += digits
    if input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет): ').lower() in ['да', 'д', 'yes']:
        chars += uppercase_letters
    if input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет): ').lower() in ['да', 'д', 'yes']:
        chars += lowercase_letters
    if input('Включать ли символы !#$%&*+-=?@^_? (да/нет): ').lower() in ['да', 'д', 'yes']:
        chars += punctuation
    if input('Исключать ли неоднозначные символы il1Lo0O? (да/нет): ').lower() in ['да', 'д', 'yes']:
        for ch in 'il1Lo0O':
            chars = chars.replace(ch, '')
    
    return chars, lenght
    
def generate_password(chars, length):
    return ''.join(random.sample(chars, length))

count = int(input('Введите количество требуемых паролей'))
chars, length = parametrs()

for _ in range(count):
    print(generate_password(chars, length))