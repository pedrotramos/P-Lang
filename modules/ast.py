class Block:
    def __init__(self, expressions):
        self.expressions = expressions

    def eval(self):
        self.expressions.eval()


class ExpressionSequence:
    def __init__(self, expressions):
        self.expressions = expressions


class Number:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Bool:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return bool(self.value)


class UnaryOperation:
    def __init__(self, child):
        self.child = child


class Positive(UnaryOperation):
    def eval(self):
        return self.child.eval()


class Negative(UnaryOperation):
    def eval(self):
        return -(self.child.eval())


class NotOp(UnaryOperation):
    def eval(self):
        return not self.child.eval()


class BinaryOperation:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOperation):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOperation):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Multi(BinaryOperation):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOperation):
    def eval(self):
        return int(self.left.eval() / self.right.eval())


class EqComp(BinaryOperation):
    def eval(self):
        return self.left.eval() == self.right.eval()


class NeqComp(BinaryOperation):
    def eval(self):
        return self.left.eval() != self.right.eval()


class GteComp(BinaryOperation):
    def eval(self):
        return self.left.eval() >= self.right.eval()


class GtComp(BinaryOperation):
    def eval(self):
        return self.left.eval() > self.right.eval()


class LteComp(BinaryOperation):
    def eval(self):
        return self.left.eval() <= self.right.eval()


class LtComp(BinaryOperation):
    def eval(self):
        return self.left.eval() < self.right.eval()


class AndOp(BinaryOperation):
    def eval(self):
        return self.left.eval() and self.right.eval()


class OrOp(BinaryOperation):
    def eval(self):
        return self.left.eval() or self.right.eval()


class IfElseOp:
    def __init__(self, condition, commands, else_commands=None):
        self.condition = condition
        self.commands = commands
        self.else_commands = else_commands

    def eval(self):
        if self.condition.eval():
            self.commands.eval()
        else:
            if self.else_commands != None:
                self.else_commands.eval()


class WhileOp:
    def __init__(self, condition, commands):
        self.condition = condition
        self.commands = commands

    def eval(self):
        while self.children[0].eval():
            self.children[1].eval()


class Print:
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())