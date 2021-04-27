# Swift em Português Brasileiro

## EBNF

~~~
BLOCK = { COMMAND } ;
COMMAND = ( λ | ASSIGNMENT | EXPRESSION | LOOP-STATEMENT | DECLARATION | IF-STATEMENT | PRINT | RETURN ) ;
TYPE = ( "Inteiro" | "Decimal" | "Booleano" | "Texto" | CLASS-NAME ) ;
CLASS-NAME = IDENTIFIER ;
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
LOOP-STATEMENT = ( FOR-IN-STATEMENT | WHILE-STATEMENT ) ;
FOR-IN-STATEMENT = "para", PATTERN, "em", EXPRESSION, "{" BLOCK "}" ; 
WHILE-STATEMENT = "enquanto", CONDITION-LIST, "{" BLOCK "}" ; 
DECLARATION = ( IMPORT-DECLARATION | FUNCTION-DECLARATION ) ;
IMPORT-DECLARATION = "importar", IMPORT-PATH ;
IMPORT-PATH = ( IDENTIFIER | IDENTIFIER, ".", IMPORT-PATH ) ;
FUNCTION-DECLARATION = "funcao", FUNCTION-NAME, "(", PARAMETER-LIST, ")", "->" TYPE, "{" BLOCK "}" ; 
PARAMETER-LIST = PARAMETER-NAME, ":", TYPE, { ",", PARAMETER-LIST } ;
IF-STATEMENT = "se", CONDITION-LIST, "{" BLOCK,"}"  { ELSE-STATEMENT } ;
ELSE-STATEMENT = ( "senao", "{" BLOCK "}" | "senao", IF-STATEMENT ) ;
CONDITION-LIST = ( CONDITION | CONDITION, CONDITION-LIST ) ;
CONDITION = ( EXPRESSION, LOGICAL-OPERATOR, EXPRESSION | LOGICAL-OPERATOR, EXPRESSION ) ;
OPERATOR = ( ARITHIMETIC-OPERATOR | LOGICAL-OPERATOR )
UNARY-OPERATOR = ( "+" | "-" ) ;
ARITHIMETIC-OPERATOR = ( UNARY-OPERATOR | "*" | "/" | "%" ) ;
LOGICAL-OPERATOR = ( ">" | "<" | ">=" | "<=" | "==" | "!=" | "&&" | "||" | "!" ) ;
PRINT = "imprima", "(", EXPRESSION, ")" ;
RETURN = "retorne", { EXPRESSION };
EXPRESSION = { UNARY-OPERATOR }, ( NUMBER | IDENTIFIER ), { OPERATOR, ( NUMBER | IDENTIFIER ) }, ";" ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
~~~
