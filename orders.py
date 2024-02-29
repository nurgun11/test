import math


class Order:
    def __init__(self, from_location, to_location, cost):
        self.from_location = from_location
        self.to_location = to_location
        self.cost = cost


class Courier:
    def __init__(self, location):
        self.location = location


def distribute_orders(orders, couriers):
    distributed_orders = []

    for order in orders:
        min_distance = float("inf")
        chosen_courier = None

        for courier in couriers:
            distance = calculate_distance(
                courier.location, order.from_location)
            if distance < min_distance:
                min_distance = distance
                chosen_courier = courier

        distributed_orders.append((order, chosen_courier))

    return distributed_orders


def calculate_distance(point1, point2):
    a1, b1 = point1
    a2, b2 = point2
    return math.sqrt((a2 - a1) ** 2 + (b2 - b1) ** 2)


orders = [
    Order((85, 75), (95, 85), 100),
    Order((65, 45), (75, 50), 200),
    Order((35, 25), (55, 45), 300),
]

couriers = [
    Courier((25, 15)),
    Courier((55, 35)),
    Courier((75, 65)),
]

distributed_orders = distribute_orders(orders, couriers)

for order, courier in distributed_orders:
    print(f"Заказ с координатами {
          order.from_location} и стоимостью {order.cost} руб. принят курьером с координатами {courier.location}")
