"""Функция принимает строку и возвращает словарь, где ключами являются символы, а значениями - их частота в строке."""
def char_frequency(s: str) -> dict:
    result = {ch: s.count(ch) for ch in s}
    return result

s = "abracadabra"
print(char_frequency(s))
