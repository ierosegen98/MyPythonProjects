def filtered_set_diff(set1: set, set2: set, filter_func: callable) -> frozenset:
    """Возвращает неизменяемое множество элементов разности двух множеств, удовлетворяющих заданному условию фильтрации."""
    return frozenset(filter(filter_func, set1 - set2))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6}
filter_even = lambda x: x % 2 == 0
print("Тест:", filtered_set_diff(set_a, set_b, filter_even))