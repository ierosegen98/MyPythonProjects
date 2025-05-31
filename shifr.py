en_upper = [chr(i) for i in range(65, 91)] 
en_lower = [chr(i) for i in range(97, 123)]    
ru_upper = [chr(i) for i in range(1040, 1072)] 
ru_lower = [chr(i) for i in range(1072, 1104)]

def parametrs():
    action = input('Вы хотите зашифровать данные (1) или расшифровать (2)? ').strip()
    shifr = action == '1'

    lang_input = input('Укажите язык шифра: ').strip().lower()
    if lang_input in ['русский', 'ру', 'ru']:
        language = 'ru'
    else:
        language = 'en'

    sdvig = int(input('Введите шаг сдвига(вправо):'))
    return shifr, language, sdvig

def shifrovanie(shifr, language, sdvig):
    result = ''
    text = input('Введите текст: ')

    if language == 'ru':
        upper_alphabet = ru_upper
        lower_alphabet = ru_lower
    else:
        upper_alphabet = en_upper
        lower_alphabet = en_lower

    for char in text:
        if char in upper_alphabet:
            alphabet = upper_alphabet
        elif char in lower_alphabet:
            alphabet = lower_alphabet
        else:
            result += char
            continue

        index = alphabet.index(char)
        shift = sdvig if shifr else -sdvig
        new_index = (index + shift) % len(alphabet)
        result += alphabet[new_index]

    return result

shifr, language, sdvig = parametrs()
result = shifrovanie(shifr, language, sdvig)
print("Результат:", result)

    
                
                
