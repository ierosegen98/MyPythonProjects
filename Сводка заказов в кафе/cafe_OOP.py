class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, name, balance, orders=None):
        self.name = name
        self.__balance = balance
        self.orders = orders or []

    def add_balance(self, amount):
        self.__balance += amount

    def make_payment(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            raise ValueError(f"Недостаточно средств для списания {amount}. Текущий баланс: {self.__balance}")
        
    def get_balance(self):
        return self.__balance

class Cart:
    def __init__(self, *products):
        self.products = list(products)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self,product):
        if product in self.products:
            del self.products[self.products.index(product)]
        else:
            raise ValueError(f"Продукт {product.name} не найден в корзине")

    def _total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    
    def get_total(self):
        return self._total()

class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.status = 'new'

    def _check_payment(self):
        amount = self.cart.get_total()
        if self.user.get_balance() >= amount:
            return True
        else:
            print('Недостаточно средств')
            return False

    def pay(self):
        if self.status != 'new':
            raise ValueError("Заказ уже оплачен")
        
        amount = self.cart.get_total()
        try:
            self.user.make_payment(amount)
            self.status = 'paid'
            self.user.orders.append(self)
        except ValueError as e:
            raise ValueError(f"Оплата не прошла: {e}")


# Товары
book = Product("Book", 300)
pen = Product("Pen", 50)
notebook = Product("Notebook", 150)
lamp = Product("Lamp", 500)

# Пользователи
john = User("John", 600)
emma = User("Emma", 200)

# Корзины
cart_john = Cart(book, pen)
cart_john.add_product(notebook)   # John добавил блокнот
cart_john.remove_product(pen)     # John убрал ручку

cart_emma = Cart(lamp, pen)       # Emma добавила лампу и ручку

# Создание заказов
order_john = Order(john, cart_john)
order_emma = Order(emma, cart_emma)

# Проверка работы твоих методов
print("Баланс John до оплаты:", john.get_balance())
print("Статус заказа John до оплаты:", order_john.status)
order_john.pay()
print("Баланс John после оплаты:", john.get_balance())
print("Статус заказа John после оплаты:", order_john.status)

print("---")

print("Баланс Emma до оплаты:", emma.get_balance())
order_emma.pay()  # Баланс Emma < сумма заказа
emma.add_balance(400)
order_emma.pay()
print("Баланс Emma после пополнения и оплаты:", emma.get_balance())
print("Статус заказа Emma после оплаты:", order_emma.status)





