from collections import Counter


def char_frequency(text: str) -> dict[str, int]:
    """Возвращает частоту каждого символа в строке."""
    count = Counter(text)
    return dict(count)

text = "abracadabra"
print(char_frequency(text))
