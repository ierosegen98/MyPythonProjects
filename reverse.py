"""Функция принимает строку и возвращает её, но со словами в обратном порядке."""
def reverse_words(s: str) -> str:
    s = s.split()
    s = s[::-1]
    return ' '.join(s)

s = "Hello world from Python"
print(reverse_words(s))