class Num:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def to_infix(self):
        return str(self.value)

    def eval(self):
        return int(self.value)


class BinOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.op} {self.left!r} {self.right!r})"

    def to_infix(self):
        return f"({self.left.to_infix()} {self.op} {self.right.to_infix()})"

    def eval(self):
        l, r = self.left.eval(), self.right.eval()
        return l + r if self.op == '+' else l * r
