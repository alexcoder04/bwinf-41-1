#!/usr/bin/env python3

# not sure if this really works as intended

from utils import avg, read_data
from bsqueues import FiFoQueue, FiSoQueue, BaseQueue

def run(QueueType: BaseQueue, example: int = 0, verbose: bool = False):
    orders = QueueType()

    for i in read_data(example):
        orders.put(i)

    order_stats = []
    while not orders.empty():
        current_order = orders.get()
        if verbose:
            print(f"{orders.get_time()}, starting {current_order}")
        orders.tick(current_order.length)
        if verbose:
            print(f"{orders.get_time()}, finished {current_order} in {orders.get_time() - current_order.start}/{orders.get_time() - current_order.start-current_order.length}")
        order_stats.append((current_order, orders.get_time() - current_order.start))

    wartezeiten = []
    for i in order_stats:
        if verbose:
            print(f"{i[0]} in {i[1]}/{i[1]-i[0].length}")
        wartezeiten.append(i[1])

    print(f" --- Example {example} using {orders.type} --- ")
    print("avg:", avg(wartezeiten))
    print("max:", max(wartezeiten))

if __name__ == "__main__":
    for i in range(5):
        run(FiFoQueue, example=i, verbose=False)
        run(FiSoQueue, example=i, verbose=False)
