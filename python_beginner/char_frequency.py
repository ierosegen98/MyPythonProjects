"""Функция принимает строку и возвращает словарь, где ключами являются символы, а значениями - их частота в строке."""
from collections import Counter

def char_frequency(s: str) -> dict:
    count = Counter(s)
    return dict(count)

s = "abracadabra"
print(char_frequency(s))
