class Jar:
    def __init__(self, capacity=12,size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return self.size*"🍪"

    def deposit(self, n):
        if (self.capacity-self._size)>= n:
            self._size += n
            # return self.size
        else: raise ValueError("Trying to put more than the capacity")

    def withdraw(self, n):
        if self._size>= n  :
            self._size -= n
            # return self.size
        else: raise ValueError("Cannot withdraw more than the capacity")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity <0 :
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        self._size = size

# def main():
#     ...

# if __name__ == "__name__":
#     main()
