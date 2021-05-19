from modules.ast import (
    AndOp,
    Block,
    Bool,
    Div,
    EqComp,
    GtComp,
    GteComp,
    Identifier,
    IfElseOp,
    LtComp,
    LteComp,
    Multi,
    Negative,
    NeqComp,
    NotOp,
    Number,
    OrOp,
    Positive,
    Print,
    Rem,
    String,
    Sub,
    Sum,
    Variable,
    WhileOp,
)

from modules.symbol_table import SymbolTable

from rply import ParserGenerator


class Parser:
    def __init__(self):
        self.pgen = ParserGenerator(
            # A list of all token names accepted by the parser.
            [
                "STRING",
                "BOOL",
                "NUMBER",
                "PRINT",
                "OPEN_PAREN",
                "CLOSE_PAREN",
                "EOL",
                "SUM",
                "SUB",
                "MULTI",
                "DIV",
                "REM",
                "AND",
                "OR",
                "WHILE",
                "IF",
                "ELSE",
                "EQ_COMP",
                "NEQ_COMP",
                "GTE_COMP",
                "LTE_COMP",
                "NOT",
                "LT_COMP",
                "GT_COMP",
                "IDENTIFIER",
                "VAR",
                "OPEN_BLOCK",
                "CLOSE_BLOCK",
            ],
            precedence=[
                ("left", ["OR"]),
                ("left", ["AND"]),
                ("left", ["EQ_COMP", "NEQ_COMP"]),
                ("left", ["GTE_COMP", "GT_COMP", "LTE_COMP", "LT_COMP"]),
                ("left", ["SUM", "SUB"]),
                ("left", ["MULTI", "DIV", "REM"]),
            ],
        )
        self.symbols = SymbolTable()

    def parse(self):
        @self.pgen.production("block : OPEN_BLOCK CLOSE_BLOCK")
        @self.pgen.production("block : OPEN_BLOCK expression_seq CLOSE_BLOCK")
        def block(p):
            def parse_expressions(exps):
                expressions = [exps[0]]
                if len(exps) > 2:
                    new_exps = parse_expressions(exps[2])
                    for exp in new_exps:
                        expressions.append(exp)
                    return expressions
                else:
                    if type(exps[1]) == type(list()):
                        new_exps = parse_expressions(exps[1])
                        for exp in new_exps:
                            expressions.append(exp)
                        return expressions
                    return [exps[0]]

            if len(p) >= 3:
                expressions = parse_expressions(p[1])
                return Block(expressions)
            else:
                return Block([])

        @self.pgen.production("expression_seq : expression EOL")
        @self.pgen.production("expression_seq : expression EOL expression_seq")
        @self.pgen.production("expression_seq : println EOL")
        @self.pgen.production("expression_seq : println EOL expression_seq")
        @self.pgen.production("expression_seq : while")
        @self.pgen.production("expression_seq : while expression_seq")
        @self.pgen.production("expression_seq : if_else")
        @self.pgen.production("expression_seq : if_else expression_seq")
        def expression_seq(p):
            if len(p) == 2:
                return p
            else:
                return p

        @self.pgen.production("println : PRINT OPEN_PAREN expression CLOSE_PAREN")
        def println(p):
            return Print(p[2])

        @self.pgen.production("expression : VAR IDENTIFIER expression")
        @self.pgen.production("expression : expression SUM expression")
        @self.pgen.production("expression : expression SUB expression")
        @self.pgen.production("expression : expression MULTI expression")
        @self.pgen.production("expression : expression DIV expression")
        @self.pgen.production("expression : expression REM expression")
        @self.pgen.production("expression : expression EQ_COMP expression")
        @self.pgen.production("expression : expression NEQ_COMP expression")
        @self.pgen.production("expression : expression GTE_COMP expression")
        @self.pgen.production("expression : expression GT_COMP expression")
        @self.pgen.production("expression : expression LTE_COMP expression")
        @self.pgen.production("expression : expression LT_COMP expression")
        @self.pgen.production("expression : expression AND expression")
        @self.pgen.production("expression : expression OR expression")
        def bin_expression(p):
            if p[1].gettokentype() == "IDENTIFIER":
                return Identifier(p[0].value, p[2], self.symbols)
            if p[1].gettokentype() == "SUM":
                return Sum(p[0], p[2])
            elif p[1].gettokentype() == "SUB":
                return Sub(p[0], p[2])
            elif p[1].gettokentype() == "MULTI":
                return Multi(p[0], p[2])
            elif p[1].gettokentype() == "DIV":
                return Div(p[0], p[2])
            elif p[1].gettokentype() == "REM":
                return Rem(p[0], p[2])
            elif p[1].gettokentype() == "EQ_COMP":
                return EqComp(p[0], p[2])
            elif p[1].gettokentype() == "NEQ_COMP":
                return NeqComp(p[0], p[2])
            elif p[1].gettokentype() == "GTE_COMP":
                return GteComp(p[0], p[2])
            elif p[1].gettokentype() == "GT_COMP":
                return GtComp(p[0], p[2])
            elif p[1].gettokentype() == "LTE_COMP":
                return LteComp(p[0], p[2])
            elif p[1].gettokentype() == "LT_COMP":
                return LtComp(p[0], p[2])
            elif p[1].gettokentype() == "AND":
                return AndOp(p[0], p[2])
            elif p[1].gettokentype() == "OR":
                return OrOp(p[0], p[2])

        @self.pgen.production("expression : NOT expression")
        @self.pgen.production("expression : SUM expression")
        @self.pgen.production("expression : SUB expression")
        def un_expression(p):
            if p[0].gettokentype() == "NOT":
                return NotOp(p[1])
            elif p[0].gettokentype() == "SUM":
                return Positive(p[1])
            elif p[0].gettokentype() == "SUB":
                return Negative(p[1])

        @self.pgen.production("expression : OPEN_PAREN expression CLOSE_PAREN")
        @self.pgen.production(
            "expression : OPEN_PAREN expression CLOSE_PAREN expression"
        )
        def paren_exp(p):
            return p[1]

        @self.pgen.production("if_else : IF OPEN_PAREN expression CLOSE_PAREN block")
        @self.pgen.production(
            "if_else : IF OPEN_PAREN expression CLOSE_PAREN block ELSE block"
        )
        def if_else(p):
            if len(p) == 5:
                return IfElseOp(p[2], p[4])
            else:
                return IfElseOp(p[2], p[4], p[6])

        @self.pgen.production("while : WHILE OPEN_PAREN expression CLOSE_PAREN block")
        def while_loop(p):
            return WhileOp(p[2], p[4])

        @self.pgen.production("expression : VAR")
        def number(p):
            return Variable(p[0].value, self.symbols)

        @self.pgen.production("expression : NUMBER")
        def number(p):
            return Number(p[0].value)

        @self.pgen.production("expression : BOOL")
        def boolean(p):
            return Bool(p[0].value)

        @self.pgen.production("expression : STRING")
        def string(p):
            return String(p[0].value)

        @self.pgen.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pgen.build()
