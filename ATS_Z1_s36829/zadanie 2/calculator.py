class Calculator:
    OPERATIONS = ("+", "-", "*", "/")

    def __init__(self, a, b, op: str):
        for x in (a, b):
            if isinstance(x, bool) or not isinstance(x, (int, float)):
                raise TypeError("Operands must be numbers")
        if op not in self.OPERATIONS:
            raise ValueError(f"Unsupported operation: {op}")
        self.a = a
        self.b = b
        self.op = op

    def calculate(self) -> float:
        if self.op == "+":
            return self.a + self.b
        if self.op == "-":
            return self.a - self.b
        if self.op == "*":
            return self.a * self.b
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.a / self.b