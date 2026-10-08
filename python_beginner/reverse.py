
def reverse_words(text: str) -> str:
    """Возвращает строку со словами в обратном порядке."""
    reversed_words = text.split()[::-1]
    return ' '.join(reversed_words)

text = "Hello world from Python"
print(reverse_words(text))