"""Функция принимает две строки и проверяет, являются ли они анаграммами."""
from collections import Counter

def are_anagrams(s1: str, s2: str) -> bool:
    s1_dict = dict(Counter(s1.lower()))
    s2_dict = dict(Counter(s2.lower()))
    return s1_dict == s2_dict

# Тест
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  
