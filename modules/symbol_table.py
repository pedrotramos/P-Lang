class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def getSymbol(self, f, s):
        if s in self.symbols[f]["vars"]:
            return self.symbols[f]["vars"][s]
        else:
            print(f, s)
            raise ValueError("Tentando ler uma variável não inicializada")

    def getFunctionParam(self, f, param):
        if f in self.symbols:
            if param in self.symbols["params"]:
                return self.symbols[f]["params"][param]
            else:
                raise ValueError("Tentando ler um parâmetro inexistente")
        else:
            raise ValueError("Tentando ler uma função não declarada")

    def getFunctionParams(self, f):
        if f in self.symbols:
            return self.symbols[f]["params"]
        else:
            raise ValueError("Tentando ler uma função não declarada")

    def getFunctionStmts(self, f):
        if f in self.symbols:
            return self.symbols[f]["stmts"]
        else:
            raise ValueError("Tentando ler uma função não declarada")

    def setSymbol(self, function, name, value):
        self.symbols[function]["vars"][name] = value

    def setFunction(self, name, parameters):
        exists = False
        try:
            exists = self.symbols[name]
        except:
            pass
        if exists:
            raise Exception(f"A função {name} está sendo declarada mais de uma vez")
        self.symbols[name] = {
            "params": parameters,
            "vars": {},
        }

    def setFunctionStmts(self, name, statements):
        self.symbols[name]["stmts"] = statements
