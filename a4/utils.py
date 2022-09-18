import queue

class Order:
    def __init__(self, start: int, length: int):
        self.start = start
        self.length = length
    
    def __str__(self):
        return f"Order({self.start}|{self.length})"
    
    def __repr__(self):
        return self.__str__()

def read_data(number: int) -> list[Order]:
    with open(f"./material/Aufgabe4/fahrradwerkstatt{number}.txt") as f:
        lines = f.readlines()
    orders = []
    for i in lines:
        if i.strip() == "":
            continue
        orders.append(Order(*[int(j) for j in i.strip().split()]))
    return orders

def avg(l: list[int]) -> int:
    s = 0
    for i in l:
        s += i
    return int(s / len(l))
