from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Function Declaration
        self.lexer.add("FUNCTION", r"funcao(?![\w])")
        # Parameter Separator
        self.lexer.add("SEP", r"\,")
        # Return
        self.lexer.add("RETURN", r"retorne(?![\w])")
        # Print
        self.lexer.add("PRINT", r"imprima(?![\w])")
        # While
        self.lexer.add("WHILE", r"enquanto(?![\w])")
        # If-Else
        self.lexer.add("ELSE", r"senao(?![\w])")
        self.lexer.add("IF", r"se(?![\w])")
        # Bool
        self.lexer.add("BOOL", r"(verdadeiro(?![\w])|falso(?![\w]))")
        # String
        self.lexer.add("STRING", r"\".*\"")
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
        self.lexer.add("REM", r"\%")
        # Logical Opertors
        self.lexer.add("EQ_COMP", r"\=\=")
        self.lexer.add("NEQ_COMP", r"\!\=")
        self.lexer.add("GTE_COMP", r"\>\=")
        self.lexer.add("LTE_COMP", r"\<\=")
        self.lexer.add("GT_COMP", r"\>")
        self.lexer.add("LT_COMP", r"\<")
        self.lexer.add("AND", r"e(?![\w])")
        self.lexer.add("OR", r"ou(?![\w])")
        self.lexer.add("NOT", r"nao(?![\w])")
        # Variables
        self.lexer.add("IDENTIFIER", r"[a-zA-Z_$][a-zA-Z_$0-9]*")
        # Identifier
        self.lexer.add("ATTRIBUTION", r"\=")
        # Number
        self.lexer.add("NUMBER", r"\d+")
        # Ignore spaces
        self.lexer.ignore("\s+")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
