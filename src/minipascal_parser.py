import ply.yacc as yacc
from lexer import tokens
import lexer
import sys

VERBOSE = 1 # 1 para imprimir errores, 0 para no imprimir errores

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
                   | procedure_declaration
                   | type_declaration'''
    pass

def p_var_declaration(p):
    'var_declaration : VAR var_decl_list SEMICOLON'
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
    'const_declaration : CONST const_list SEMICOLON'
    pass

def p_const_list(p):
    '''const_list : const_list COMMA ID EQUAL constant
                  | ID EQUAL constant'''
    pass

def p_procedure_declaration(p):
    'procedure_declaration : PROCEDURE ID LPAREN param_list RPAREN SEMICOLON block'
    pass

def p_type_declaration(p):
    'type_declaration : TYPE ID EQUAL type SEMICOLON'
    pass

def p_param_list(p):
    '''param_list : param_list SEMICOLON param
                  | param
                  | empty'''
    pass

def p_param(p):
    'param : ID COLON type'
    pass

# Reglas para las declaraciones de tipo
def p_type(p):
    '''type : INTEGER
            | REAL
            | BOOLEAN
            | STRING
            | ARRAY LBRACKET INTEGER_CONST RBRACKET OF type
            | RECORD record_fields END
            | SET LBRACKET type RBRACKET'''
    pass

def p_record_fields(p):
    '''record_fields : record_fields var_declaration
                     | var_declaration'''
    pass

# Reglas para la lista de sentencias
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

# Reglas para las sentencias
def p_statement(p):
    '''statement : assignment_statement
                 | if_statement
                 | while_statement
                 | repeat_statement
                 | for_statement
                 | procedure_call
                 | record_assignment
                 | empty'''
    pass

def p_assignment_statement(p):
    'assignment_statement : ID ASSIGN expression SEMICOLON'
    pass

def p_record_assignment(p):
    'record_assignment : ID DOT ID ASSIGN expression SEMICOLON'
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
    'for_statement : FOR ID ASSIGN expression TO expression DO statement'
    pass

def p_procedure_call(p):
    'procedure_call : ID LPAREN args RPAREN SEMICOLON'
    pass

def p_args(p):
    '''args : args COMMA expression
            | expression
            | empty'''
    pass

# Reglas para las expresiones
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DIVIDE_INT expression
                  | expression MODULO expression
                  | expression EQUAL expression
                  | expression NEQUAL expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression AND expression
                  | expression OR expression
                  | expression XOR expression'''
    pass

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    pass

def p_expression_literal(p):
    '''expression : INTEGER_CONST
                  | REAL_CONST
                  | STRING_LITERAL
                  | ID'''
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
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		
parser = yacc.yacc(debug=True)

if __name__ == '__main__':
	if (len(sys.argv) > 1):
          
		fin = sys.argv[1]
	else:
		fin = '/workspaces/MINIPASCAL-LEX/examples/example2.pas'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("El parser reconoció correctamente todo")
	#input()
