class User:
    def __init__(self, id, name, email, shopping_cart=None):
        self.id = id
        self.name = name
        self.email = email
        self.shopping_cart = shopping_cart


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self, id, user_id, orders):
        self.id = id
        self.user_id = user_id
        self.orders = orders

    def calculate_the_total_price(self):
        return sum([order.product.price * order.amount
                    for order in self.orders])

    def add_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        try:
            self.orders.remove(order)
        except ValueError:
            print('Product not found !')

    def remove_product(self, product_id, sub_amount):
            for order in self.orders:
                if order.product.id == product_id:
                    if order.amount < sub_amount:
                        print('Not enough products in shopping cart !')
                    else:
                        order.amount = order.amount - sub_amount


class Order:
    def __init__(self, id, product, amount):
        self.id = id
        self.product = product
        self.amount = amount


def main():
    user1 = User('u001', 'John Doe', 'john.doe@example.com')
    product1 = Product('p001', 'Apple', 4.95)
    product2 = Product('p002', 'Orange', 3.99)

    # Test case 1
    order1 = Order('o001', product1, 2)
    order2 = Order('o002', product2, 1)

    shopping_cart1 = ShoppingCart('s001', user1.id, [order1, order2])

    print('Test case 1: Total price: {}'
          .format(shopping_cart1.calculate_the_total_price()))

    # Test case 2
    order3 = Order('o003', product1, 3)

    shopping_cart2 = ShoppingCart('s002', user1.id, [order3])
    shopping_cart2.remove_product(product1.id, 1)

    print('Test case 2: Total price: {}'
          .format(shopping_cart2.calculate_the_total_price()))


if __name__ == '__main__':
    main()

