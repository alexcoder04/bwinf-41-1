import queue
from utils import Order

# TODO check current time!
class FiFoQueue:
    def __init__(self):
        self._queue = queue.Queue()
    
    def __len__(self):
        return self._queue.qsize()
    
    def put(self, element: Order):
        self._queue.put(element)
    
    def get(self):
        return self._queue.get()

# TODO check current time!
class FiSoQueue:
    def __init__(self):
        self._orders = []
    
    def __len__(self):
        return len(self._orders)
    
    def put(self, element: Order):
        self._orders.append(element)
    
    def get(self):
        min_len = 1000000
        min_el_num = None
        for i, e in enumerate(self._orders):
            if e.length < min_len:
                min_len = e.length
                min_el_num = i
        result = self._orders[min_el_num]
        new_orders = []
        for i, e in enumerate(self._orders):
            if i == min_el_num:
                continue
            new_orders.append(e)
        self._orders = new_orders
        return result
