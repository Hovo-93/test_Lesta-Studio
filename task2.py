"""
2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO.
Объяснить плюсы и минусы каждой реализации.
"""


class My_queue:

    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def add(self, value):
        self.elements.append(value)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError
        return self.elements.pop(0)


"""
Списки слишком медленные для этой задачи, так как вставка и удаление элемента с начала требует сдвига всех
прочих элементов по одному, на это уходит О(n) времени.
"""
