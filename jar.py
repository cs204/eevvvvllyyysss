class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Емкость должна быть неотрицательным целым числом.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Количество печений для добавления должно быть неотрицательным.")
        if self._size + n > self._capacity:
            raise ValueError("Превышение емкости банки.")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Количество печений для удаления должно быть неотрицательным.")
        if n > self._size:
            raise ValueError("Недостаточно печений в банке для удаления.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

