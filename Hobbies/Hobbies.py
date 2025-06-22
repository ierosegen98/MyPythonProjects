users = {
    'Аня': {'чтение', 'плавание', 'фехтование'},
    'Борис': {'плавание', 'шахматы', 'программирование'},
    'Вера': {'фехтование', 'рисование', 'шахматы'},
    'Глеб': {'чтение', 'программирование', 'фехтование'},
}

def unique_hobbies(users, union):
    unique = set()
    hobbies = {i : 0 for i in union}
    for hobby in hobbies:
        for name in users:
            if hobby in users[name]:
                hobbies[hobby] += 1

    for hobby in hobbies:
        if hobbies[hobby] == 1:
            unique.add(hobby)

    return unique, hobbies

def inters(users):
    inter = next(iter(users.values()))

    for name in users:
        inter &= users[name]

    return inter

def pairs(users):
    pair = []
    max = 0
    cur_pair = set()

    for name in users:
        for name_2 in users:
            if name != name_2:
                cur_pair = users[name].intersection(users[name_2])
                if len(cur_pair) > max:
                    max = len(cur_pair)
                    pair = []
                    pair.append(name)
                    pair.append(name_2)
                if max == 3:
                    break

    return pair

def all_hobbies(users):
    union = set()

    for name in users:
        union |= users[name]

    return union

union = all_hobbies(users)
unique, hobbies = unique_hobbies(users, union)    
pair = pairs(users)
inter = inters(users)


print(*unique)
print(*inter)
print(*pair)
print(*sorted(union))
for hobby in sorted(hobbies):
    print(f"{hobby}: {hobbies[hobby]}")