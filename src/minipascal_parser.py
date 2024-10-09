import ply.yacc as yacc
from lexer import tokens
import lexer
import sys

VERBOSE = 1  # 1 para imprimir errores, 0 para no imprimir errores

# Precedencia de operadores
precedence = (
    ('right', 'ASSIGN'),
    ('left', 'OR', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'EQUAL', 'NEQUAL', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'DIVIDE_INT', 'MODULO'),
    ('left', 'SHL', 'SHR'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
)

# Reglas para el programa principal
def p_program(p):
    'program : PROGRAM ID SEMICOLON block DOT'
    pass

# Reglas para el bloque
def p_block(p):
    'block : declarations BEGIN statement_list END'
    pass

# Reglas para las declaraciones
def p_declarations(p):
    '''declarations : declarations declaration
                    | empty'''
    pass

def p_declaration(p):
    '''declaration : var_declaration
                   | const_declaration
                   | type_declaration
                   | procedure_declaration
                   | function_declaration
                   | uses_clause'''
    pass

def p_uses_clause(p):
    'uses_clause : USES identifier_list SEMICOLON'
    pass

def p_identifier_list(p):
    '''identifier_list : identifier_list COMMA ID
                       | ID'''
    pass

def p_var_declaration(p):
    'var_declaration : VAR var_decl_list'
    pass

def p_var_decl_list(p):
    '''var_decl_list : var_decl_list var_decl
                     | var_decl'''
    pass

def p_var_decl(p):
    'var_decl : id_list COLON type SEMICOLON'
    pass

def p_id_list(p):
    '''id_list : id_list COMMA ID
               | ID'''
    pass

def p_const_declaration(p):
    'const_declaration : CONST const_list'
    pass

def p_const_list(p):
    '''const_list : const_list const_decl
                  | const_decl'''
    pass

def p_const_decl(p):
    'const_decl : ID EQUAL constant SEMICOLON'
    pass

def p_type_declaration(p):
    'type_declaration : TYPE type_decl_list'
    pass

def p_type_decl_list(p):
    '''type_decl_list : type_decl_list type_decl
                      | type_decl'''
    pass

def p_type_decl(p):
    'type_decl : ID EQUAL type SEMICOLON'
    pass

def p_procedure_declaration(p):
    '''procedure_declaration : PROCEDURE ID SEMICOLON block SEMICOLON
                             | PROCEDURE ID LPAREN param_list RPAREN SEMICOLON block SEMICOLON'''
    pass

def p_function_declaration(p):
    '''function_declaration : FUNCTION ID COLON type SEMICOLON block SEMICOLON
                            | FUNCTION ID LPAREN param_list RPAREN COLON type SEMICOLON block SEMICOLON'''
    pass

def p_param_list(p):
    '''param_list : param_list SEMICOLON param
                  | param'''
    pass

def p_param(p):
    'param : id_list COLON type'
    pass

def p_type(p):
    '''type : INTEGER
            | REAL
            | BOOLEAN
            | STRING
            | ID
            | ARRAY LBRACKET range RBRACKET OF type
            | RECORD field_list END'''
    pass

def p_range(p):
    'range : INTEGER_CONST DOTDOT INTEGER_CONST'
    pass

def p_field_list(p):
    '''field_list : field_list field_decl SEMICOLON
                  | field_decl SEMICOLON'''
    pass

def p_field_decl(p):
    'field_decl : id_list COLON type'
    pass

# Reglas para la lista de sentencias
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_statement(p):
    '''statement : assignment_statement
                 | procedure_call
                 | compound_statement
                 | if_statement
                 | while_statement
                 | repeat_statement
                 | for_statement
                 | empty'''
    pass

def p_assignment_statement(p):
    'assignment_statement : variable ASSIGN expression SEMICOLON'
    pass

def p_variable(p):
    '''variable : ID
                | ID LBRACKET expression_list RBRACKET
                | ID DOT ID'''
    pass

def p_expression_list(p):
    '''expression_list : expression_list COMMA expression
                       | expression'''
    pass

def p_procedure_call(p):
    '''procedure_call : ID LPAREN args RPAREN SEMICOLON
                      | ID SEMICOLON'''
    pass

def p_args(p):
    '''args : args COMMA expression
            | expression
            | empty'''
    pass

def p_compound_statement(p):
    'compound_statement : BEGIN statement_list END'
    pass

def p_if_statement(p):
    'if_statement : IF expression THEN statement else_part'
    pass

def p_else_part(p):
    '''else_part : ELSE statement
                 | empty'''
    pass

def p_while_statement(p):
    'while_statement : WHILE expression DO statement'
    pass

def p_repeat_statement(p):
    'repeat_statement : REPEAT statement_list UNTIL expression SEMICOLON'
    pass

def p_for_statement(p):
    'for_statement : FOR ID ASSIGN expression direction expression DO statement'
    pass

def p_direction(p):
    '''direction : TO
                 | DOWNTO'''
    pass

def p_expression(p):
    'expression : simple_expression relop_opt'
    pass

def p_relop_opt(p):
    '''relop_opt : relop simple_expression
                 | empty'''
    pass

def p_relop(p):
    '''relop : EQUAL
             | NEQUAL
             | LT
             | LE
             | GT
             | GE
             | IN'''
    pass

def p_simple_expression(p):
    '''simple_expression : term
                         | simple_expression addop term'''
    pass

def p_addop(p):
    '''addop : PLUS
             | MINUS
             | OR
             | XOR'''
    pass

def p_term(p):
    '''term : factor
            | term mulop factor'''
    pass

def p_mulop(p):
    '''mulop : TIMES
             | DIVIDE
             | DIVIDE_INT
             | MODULO
             | DIV
             | MOD
             | AND
             | SHL
             | SHR'''
    pass

def p_factor(p):
    '''factor : variable
              | INTEGER_CONST
              | REAL_CONST
              | STRING_LITERAL
              | LPAREN expression RPAREN
              | NOT factor
              | MINUS factor %prec UMINUS'''
    pass

def p_constant(p):
    '''constant : INTEGER_CONST
                | REAL_CONST
                | STRING_LITERAL
                | NIL'''
    pass

# Regla para vacío
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if VERBOSE:
        if p is not None:
            print(f"ERROR SINTÁCTICO EN LA LÍNEA {p.lineno} NO SE ESPERABA EL Token '{p.value}'")
        else:
            print(f"ERROR SINTÁCTICO EN LA LÍNEA {lexer.lexer.lineno}")
    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = sys.argv[1]
    else:
        fin = '/workspaces/MINIPASCAL-LEX/examples/example2.pas'  # Ruta al archivo de ejemplo

    try:
        with open(fin, 'r') as f:
            data = f.read()
            parser.parse(data, tracking=True)
            print("El parser reconoció correctamente todo")
    except FileNotFoundError:
        print(f"Error: El archivo '{fin}' no existe.")
