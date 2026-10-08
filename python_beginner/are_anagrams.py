
from collections import Counter


def are_anagrams(string_1: str, string_2: str) -> bool:
    """Проверяет, являются ли две строки анаграммами."""
    return Counter(string_1.lower()) == Counter(string_2.lower())

string_1 = "listen"
string_2 = "silent"
print(are_anagrams(string_1, string_2))
