from copy import deepcopy


class Block:
    def __init__(self, expressions):
        self.expressions = expressions

    def eval(self, func_name):
        for expression in self.expressions:
            last = expression.eval(func_name)
            try:
                return self.symbols.getSymbol(func_name, "return")
            except:
                continue
        return last


class Number:
    def __init__(self, value):
        self.value = value

    def eval(self, func_name):
        return int(self.value)


class Bool:
    def __init__(self, value):
        self.value = value

    def eval(self, func_name):
        if self.value == "verdadeiro":
            return True
        else:
            return False


class String:
    def __init__(self, value):
        self.value = value

    def eval(self, func_name):
        return str(self.value)


class UnaryOperation:
    def __init__(self, child):
        self.child = child


class Positive(UnaryOperation):
    def eval(self, func_name):
        return self.child.eval(func_name)


class Negative(UnaryOperation):
    def eval(self, func_name):
        return -(self.child.eval(func_name))


class NotOp(UnaryOperation):
    def eval(self, func_name):
        return not self.child.eval(func_name)


class BinaryOperation:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Identifier(BinaryOperation):
    def __init__(self, left, right, s):
        self.symbols = s
        super().__init__(left, right)

    def eval(self, func_name):
        self.symbols.setSymbol(
            func_name,
            self.left,
            self.right.eval(func_name),
        )
        return


class Sum(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) + self.right.eval(func_name)


class Sub(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) - self.right.eval(func_name)


class Multi(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) * self.right.eval(func_name)


class Div(BinaryOperation):
    def eval(self, func_name):
        return int(self.left.eval(func_name) / self.right.eval(func_name))


class Rem(BinaryOperation):
    def eval(self, func_name):
        return int(self.left.eval(func_name) % self.right.eval(func_name))


class EqComp(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) == self.right.eval(func_name)


class NeqComp(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) != self.right.eval(func_name)


class GteComp(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) >= self.right.eval(func_name)


class GtComp(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) > self.right.eval(func_name)


class LteComp(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) <= self.right.eval(func_name)


class LtComp(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) < self.right.eval(func_name)


class AndOp(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) and self.right.eval(func_name)


class OrOp(BinaryOperation):
    def eval(self, func_name):
        return self.left.eval(func_name) or self.right.eval(func_name)


class IfElseOp:
    def __init__(self, condition, commands, else_commands=None):
        self.condition = condition
        self.commands = commands
        self.else_commands = else_commands

    def eval(self, func_name):
        if self.condition.eval(func_name):
            self.commands.eval(func_name)
        else:
            if self.else_commands != None:
                self.else_commands.eval(func_name)


class WhileOp:
    def __init__(self, condition, commands):
        self.condition = condition
        self.commands = commands

    def eval(self, func_name):
        while self.condition.eval(func_name):
            self.commands.eval(func_name)


class Print:
    def __init__(self, value):
        self.value = value

    def eval(self, func_name):
        print(self.value.eval(func_name))


class Variable:
    def __init__(self, value, s):
        self.symbols = s
        self.value = value

    def eval(self, func_name):
        return self.symbols.getSymbol(func_name, self.value)


class Function:
    def __init__(self, name):
        self.name = name

    def eval(self, func_name):
        return self.name


class FuncDec:
    def __init__(self, name, stmts, s):
        self.name = name
        self.statements = stmts
        self.symbols = s

    def eval(self, func_name):
        self.statements.eval(func_name)


class Parameter:
    def __init__(self, func, val, s):
        self.symbols = s
        self.func_name = func
        self.value = val

    def eval(self, func_name):
        return self.symbols.getFunctionParam(self.func_name, self.value)


class FuncCall:
    def __init__(self, func_name, children, s):
        self.name = func_name
        self.children = children
        self.symbols = s

    def eval(self, func_name):
        if len(self.children) != len(self.symbols.getFunctionParams(self.name)):
            raise ValueError(
                f"Problema com o número de argumentos na chamada da função {func_name}"
            )
        newSymbols = deepcopy(self.symbols)
        function_params = self.symbols.getFunctionParams(self.name)
        for child, param_name in zip(self.children, function_params.keys()):
            child_val = child.eval(func_name)
            newSymbols.setSymbol(self.name, param_name, child_val)
        statements = newSymbols.getFunctionStmts(self.name)
        call_output = statements.eval(self.name)
        return call_output


class Return:
    def __init__(self, expression, s):
        self.symbols = s
        self.exp = expression

    def eval(self, func_name):
        self.symbols.setSymbol(
            func_name,
            "return",
            self.exp.eval(func_name),
        )
        return self.exp.eval(func_name)


class Root:
    def __init__(self, child_list):
        self.children = child_list

    def eval(self):
        for child in self.children:
            if child.name == "principal":
                child.eval(child.name)
