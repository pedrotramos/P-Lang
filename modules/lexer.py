from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add("PRINT", r"imprima")
        # While
        self.lexer.add("WHILE", r"while")
        # If-Else
        self.lexer.add("ELSE", r"senao")
        self.lexer.add("IF", r"se")
        # Bool
        self.lexer.add("BOOL", r"(verdadeiro|falso)")
        # Variables
        self.lexer.add("VAR", r"[a-zA-Z_$][a-zA-Z_$0-9]*")
        # Block Delimiter
        self.lexer.add("OPEN_BLOCK", r"\{")
        self.lexer.add("CLOSE_BLOCK", r"\}")
        # Parenthesis
        self.lexer.add("OPEN_PAREN", r"\(")
        self.lexer.add("CLOSE_PAREN", r"\)")
        # Semi Colon
        self.lexer.add("EOL", r"\;")
        # Arithmetic Operators
        self.lexer.add("SUM", r"\+")
        self.lexer.add("SUB", r"\-")
        self.lexer.add("MULTI", r"\*")
        self.lexer.add("DIV", r"\/")
        # Logical Opertors
        self.lexer.add("EQ_COMP", r"\=\=")
        self.lexer.add("NEQ_COMP", r"\!\=")
        self.lexer.add("GTE_COMP", r"\>\=")
        self.lexer.add("LTE_COMP", r"\<\=")
        self.lexer.add("GT_COMP", r"\>")
        self.lexer.add("LT_COMP", r"\<")
        self.lexer.add("AND", r"\&\&")
        self.lexer.add("OR", r"\|\|")
        self.lexer.add("NOT", r"\!")
        # Identifier
        self.lexer.add("IDENTIFIER", r"\=")
        # Number
        self.lexer.add("NUMBER", r"\d+")
        # Ignore spaces
        self.lexer.ignore("\s+")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()