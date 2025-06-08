n = int(input("Добрый день! Спасибо, что выбрали наше кафе) Введите количество заказов: "))
orders = []

for _ in range(n):
    name = input("Введите Ваше имя:")
    item = input("Введите блюдо:")
    price = int(input("Введите стоимость:"))
    orders.append((name, item, price))

clients = []
items = []
for order in orders:
    name, item, _ = order
    items.append(item)
    if name not in clients:
        clients.append(name)



def vyruchka(orders):
    total = 0
    for i in range(len(orders)):
        total += orders[i][2]
    return total

def popularity(items):
    max_count = 0
    popular_item = ''
    mn_items = set(items)
    for item in mn_items:
        count = items.count(item)
        if count > max_count:
            max_count = count
            popular_item = item
    return f"{popular_item} ({max_count} заказа)"


def summa_zakazov(orders, clients):
    result = []
    for client in clients:
        total = sum(order[2] for order in orders if order[0] == client)
        result.append((client, total))
    return result


def more_one(orders, clients):
    clients_more_one = []
    for client in clients:
        dishes = set()
        for order in orders:
            if order[0] == client:
                dishes.add(order[1])
        if len(dishes) > 1:
            clients_more_one.append(client)
    return clients_more_one



print('\nСводка по клиентам:')
for name, total in sorted(summa_zakazov(orders, clients)):
    print(f'{name}: {total} руб.')
print('Самое популярное блюдо:', popularity(items))
print('Общая выручка:', vyruchka(orders), 'руб.')
print('Клиенты с несколькими блюдами:', *more_one(orders, clients), sep='\n')