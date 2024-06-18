def operations(name):
    return f"Hello, {name}!"

class Operations:
    def __init__(self, name):
        self.name = name
    def operations(self):
        return f"Hello, {self.name}!"
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y