#!/usr/bin/env python3

from utils import Order


class BaseQueue:
    def __init__(self) -> None:
        self._orders = []
        self._time = 0
        self.TYPE = "BASE"
    
    def __len__(self) -> int:
        return len(self._orders)

    def empty(self) -> bool:
        return len(self._orders) < 1
    
    def get_time(self) -> int:
        return self._time
    
    def tick(self, timespan: int) -> None:
        self._time += timespan
    
    def _bump_time(self, time: int) -> None:
        if time > self._time:
            self._time = time
    
    def put(self, element: Order) -> None:
        self._orders.append(element)

    def get(self) -> None:
        return
    
    def _get_next_order(self) -> (Order, int):
        min_start_time = self._orders[0].start
        next_pos = 0
        for i, e in enumerate(self._orders):
            if e.start < min_start_time:
                next_pos = i
        return self._orders[next_pos], next_pos


class FiFoQueue(BaseQueue):
    def __init__(self) -> None:
        self._orders = []
        self._time = 0
        self.type = "FIFO"
    
    def get(self) -> Order:
        result, next_pos = self._get_next_order()
        self._bump_time(result.start)
        del self._orders[next_pos]
        return result


class FiSoQueue(BaseQueue):
    def __init__(self) -> None:
        self._orders = []
        self._time = 0
        self.type = "FISO"
    
    def _get_min_curr_order(self) -> (Order, int):
        min_len = 1000000000
        min_pos = -1
        for i, e in enumerate(self._orders):
            if e.start <= self._time and e.length < min_len:
                min_len = e.length
                min_pos = i
        if min_pos == -1:
            return self._get_next_order()
        return self._orders[min_pos], min_pos
    
    def get(self) -> Order:
        result, min_pos = self._get_min_curr_order()
        self._bump_time(result.start)
        del self._orders[min_pos]
        return result
    