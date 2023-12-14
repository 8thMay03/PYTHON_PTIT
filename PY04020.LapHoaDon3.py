class Product:
    def __init__(self, id, name, num, price, discount):
        self.id = id
        self.name = name
        self. num = num
        self.price = price
        self.discount = discount
        self.total = price * num - discount
    
    def __str__(self):
        return ("{} {} {} {} {} {}").format(self.id, self.name, self.num, self.price, self.discount, self.total)

Products = []

for _ in range(int(input())):
    Products.append(Product(input(), input(), int(input()),int(input()), int(input())))

Products.sort(key=lambda x: -x.total)

for Product in Products:
    print(Product.__str__())