# P-Lang (Linguagem em Português)

## EBNF

~~~
BLOCK = "{", { COMMAND }, "}" ;
COMMAND = ( λ | ASSIGNMENT | EXPRESSION | WHILE-STATEMENT | IF-STATEMENT | PRINT ) ;
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
WHILE-STATEMENT = "enquanto", CONDITION-LIST, "{" BLOCK "}" ; 
IF-STATEMENT = "se", CONDITION-LIST, "{" BLOCK,"}"  { ELSE-STATEMENT } ;
ELSE-STATEMENT = ( "senao", "{" BLOCK "}" | "senao", IF-STATEMENT ) ;
CONDITION-LIST = ( CONDITION | CONDITION, CONDITION-LIST ) ;
CONDITION = ( EXPRESSION, LOGICAL-OPERATOR, EXPRESSION | LOGICAL-OPERATOR, EXPRESSION ) ;
OPERATOR = ( ARITHMETIC-OPERATOR | LOGICAL-OPERATOR ) ;
ARITHIMETIC-OPERATOR = ( "+" | "-" | "*" | "/" )
LOGICAL-OPERATOR = ( ">" | "<" | ">=" | "<=" | "==" | "!=" | "&&" | "||" | "!" )
PRINT = "imprima", "(", EXPRESSION, ")" ;
EXPRESSION = [( "!" | "+" | "-" )], ( IDENTIFIER | NUMBER | BOOL ), {OPERATOR, ( NUMBER | IDENTIFIER | BOOL )}, ";" ;
NUMBER = DIGIT, { DIGIT } ;
BOOL = ( "verdadeiro" | "falso" ) ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
~~~
