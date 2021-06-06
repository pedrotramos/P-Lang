import sys
from argparse import ArgumentError
from modules.lexer import Lexer
from modules.parser import Parser
from modules.ast import Root


if __name__ == "__main__":

    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], "r") as f:
                arg = f.read()
            lexer = Lexer().get_lexer()
            tokens = lexer.lex(arg)
            pg = Parser()
            pg.parse()
            parser = pg.get_parser()
            ast = Root(parser.parse(tokens))
            ast.eval()
        except:
            raise ArgumentError("Não foi possível ler o arquivo de entrada")
    else:
        raise ArgumentError("O programa precisa de um argumento para rodar")
