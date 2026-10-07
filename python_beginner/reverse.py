"""Функция принимает строку и возвращает её, но со словами в обратном порядке."""
def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

s = "Hello world from Python"
print(reverse_words(s))