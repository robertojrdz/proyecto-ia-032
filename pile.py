class Pila:
    def __init__(self):
        self.pila = []
    def push(self, value):
        if value not in self.pila:
            self.pila.append(value)
            return True
        else:
            return False
    def pop(self):
        if len(self.pila) <= 0:
            return "No element in the Stack"
        else:
            return self.pila.pop()
    def peek(self):
        return self.pila[-1]