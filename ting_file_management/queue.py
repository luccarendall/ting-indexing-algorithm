from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.fila = []

    def __len__(self):
        return len(self.fila)

    def enqueue(self, value):
        self.fila.append(value)

    def dequeue(self):
        if len(self.fila) == 0:
            return None

        return self.fila.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.fila):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.fila[index]
