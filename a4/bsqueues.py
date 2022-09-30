import queue
from utils import Order

class FiFoQueue:
    def __init__(self) -> None:
        self._queue = queue.Queue()
        self._time = 0
        self.type = "FIFO"
    
    def __len__(self) -> int:
        return self._queue.qsize()
    
    def get_time(self) -> int:
        return self._time
    
    def tick(self, timespan: int) -> None:
        self._time += timespan
    
    def put(self, element: Order) -> None:
        self._queue.put(element)
    
    # TODO get really the next, dont rely on them beeing sorted
    def get(self) -> Order:
        order = self._queue.get()
        if order.start > self._time:
            self._time = order.start
        return order
    
    def empty(self) -> bool:
        return self._queue._qsize() < 1

class FiSoQueue:
    def __init__(self) -> None:
        self._orders = []
        self._time = 0
        self.type = "FISO"
    
    def __len__(self) -> int:
        return len(self._orders)
    
    def get_time(self) -> int:
        return self._time
    
    def tick(self, timespan: int) -> None:
        self._time += timespan
    
    def put(self, element: Order) -> None:
        self._orders.append(element)
    
    def _get_next_order(self):
        min_start_time = self._orders[0].start
        min_pos = 0
        for i, e in enumerate(self._orders):
            if e.start < min_start_time:
                min_pos = i
        return min_pos
    
    def _get_min_curr_order(self) -> int:
        min_len = 1000000000
        min_pos = -1
        for i, e in enumerate(self._orders):
            if e.start <= self._time and e.length < min_len:
                min_len = e.length
                min_pos = i
        if min_pos == -1:
            min_pos = self._get_next_order()
        return min_pos
    
    def get(self) -> Order:
        min_pos = self._get_min_curr_order()
        result = self._orders[min_pos]
        if result.start > self._time:
            self._time = result.start
        new_orders = []
        for i, e in enumerate(self._orders):
            if i == min_pos:
                continue
            new_orders.append(e)
        self._orders = new_orders
        return result
    
    def empty(self) -> bool:
        return len(self._orders) < 1
