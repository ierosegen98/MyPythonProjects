import random
def collect_chars():
    chars = ''
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_.'

    if input('Включать цифры? (yes/y): ').lower() in ['yes', 'y']:
        chars += digits
    if input('Включать строчные буквы? (yes/y): ').lower() in ['yes', 'y']:
        chars += lowercase_letters
    if input('Включать прописные буквы? (yes/y): ').lower() in ['yes', 'y']:
        chars += uppercase_letters
    if input('Включать символы? (yes/y): ').lower() in ['yes', 'y']:
        chars += punctuation

    return chars

def generate_password(chars, length):
    password = random.sample(chars, length)
    return password

length = int(input('Введите длину пароля:'))
chars = collect_chars()
print(*generate_password(chars, length), sep='')