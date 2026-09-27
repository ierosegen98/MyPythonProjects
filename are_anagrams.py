"""Функция принимает две строки и проверяет, являются ли они анаграммами."""
def are_anagrams(s1: str, s2: str) -> bool:
    s1_dict = {ch: s1.count(ch) for ch in s1}
    s2_dict = {ch: s2.count(ch) for ch in s2}
    if s1_dict == s2_dict:
        return True
    else:
        return False

# Тест
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  
