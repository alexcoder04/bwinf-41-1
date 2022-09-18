from utils import avg, read_data
from bsqueues import FiFoQueue, FiSoQueue

orders = FiFoQueue()
#orders = FiSoQueue()
for i in read_data(0):
    orders.put(i)

current_time = 0
orders_stats = []
for _ in range(len(orders)):
    current_order = orders.get()
    if current_time < current_order.start:
        current_time = current_order.start
    print(f"{current_time}, starting {current_order}")
    current_time += current_order.length
    print(f"{current_time}, finished {current_order} in {current_time-current_order.start}/{current_time-current_order.start-current_order.length}")
    orders_stats.append((current_order, current_time - current_order.start))

wartezeiten = []
for i in orders_stats:
    print(f"{i[0]} in {i[1]}/{i[1]-i[0].length}")
    wartezeiten.append(i[1])

print("avg:", avg(wartezeiten))
print("max:", max(wartezeiten))
