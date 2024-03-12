class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        if name not in self.products:
            self.products[name] = price
            print(f"{name} добавлено в магазин")
        else:
            print(f"{name} уже в магазине")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"{name} удален из магазина")
        else:
            print(f"{name} его нет в магазине")

    def search_product(self, name):
        if name in self.products:
            print(f"{name} доступен в магазине {self.products[name]} рублей")
        else:
            print(f"{name} отсутствует в наличии в магазине")

    def display_products(self):
        print("Товары, доступные в магазине:")
        for name, price in self.products.items():
            print(f"{name}: {price} рублей")


shop = Shop()
shop.add_product("яблоко", 2)
shop.add_product("банан", 1)
shop.add_product("яблоко", 3)
shop.display_products()
shop.search_product("банан")
shop.search_product("апельсин")
shop.remove_product("яблоко")
shop.remove_product("апельсин")
shop.display_products()
