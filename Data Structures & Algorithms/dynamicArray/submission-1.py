class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.set(self.getSize(), n)
        self.size += 1

    def popback(self) -> int:
        if self.getSize() > 0:
            self.size -= 1
        return self.get(self.getSize())

    def resize(self) -> None:
        old = self.arr
        self.arr = old + [0] * self.getCapacity()
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity