import math


class Orders:

    @staticmethod
    def combine_orders(requests, n_max):
        if sum(requests) / n_max <= n_max:
            return math.ceil(sum(requests) / n_max)


orders = [70, 30, 10]
n_max = 100
expected_orders = 2

print(Orders.combine_orders(requests=orders, n_max=n_max))
