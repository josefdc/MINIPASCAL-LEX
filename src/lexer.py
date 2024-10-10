import ply.lex as lex
import sys

# Diccionario de palabras reservadas para evitar conflictos con identificadores
reserved = {
    'absolute': 'ABSOLUTE',
    'and': 'AND',
    'array': 'ARRAY',
    'asm': 'ASM',
    'begin': 'BEGIN',
    'boolean': 'BOOLEAN',
    'case': 'CASE',
    'const': 'CONST',
    'constructor': 'CONSTRUCTOR',
    'destructor': 'DESTRUCTOR',
    'div': 'DIV',
    'do': 'DO',
    'downto': 'DOWNTO',
    'else': 'ELSE',
    'end': 'END',
    'external': 'EXTERNAL',
    'file': 'FILE',
    'for': 'FOR',
    'forward': 'FORWARD',
    'function': 'FUNCTION',
    'goto': 'GOTO',
    'if': 'IF',
    'implementation': 'IMPLEMENTATION',
    'in': 'IN',
    'inline': 'INLINE',
    'interface': 'INTERFACE',
    'interrupt': 'INTERRUPT',
    'label': 'LABEL',
    'mod': 'MOD',
    'nil': 'NIL',
    'not': 'NOT',
    'object': 'OBJECT',
    'of': 'OF',
    'or': 'OR',
    'packed': 'PACKED',
    'procedure': 'PROCEDURE',
    'program': 'PROGRAM',
    'record': 'RECORD',
    'repeat': 'REPEAT',
    'set': 'SET',
    'shl': 'SHL',
    'shr': 'SHR',
    'string': 'STRING',
    'then': 'THEN',
    'to': 'TO',
    'type': 'TYPE',
    'unit': 'UNIT',
    'until': 'UNTIL',
    'uses': 'USES',
    'var': 'VAR',
    'virtual': 'VIRTUAL',
    'while': 'WHILE',
    'with': 'WITH',
    'xor': 'XOR',
<<<<<<< HEAD
    'div': 'DIV',
    'mod': 'MOD',
    'of' : 'OF',
=======
    'integer': 'INTEGER',
    'real': 'REAL',
>>>>>>> 14556444e3c4ee12d7c495af0295ceffdc1eaa8d
}

# Lista de tokens
tokens = [
    # Operadores
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'DIVIDE_INT', 'MODULO', 'EQUAL', 'NEQUAL',
    'LT', 'GT', 'LE', 'GE', 'ASSIGN',

    # Delimitadores
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COMMA', 'COLON', 'DOT', 'DOTDOT',

    # Otros
    'ID', 'INTEGER_CONST', 'REAL_CONST', 'STRING_LITERAL',
] + list(reserved.values())

# Reglas de expresiones regulares para tokens simples
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_DIVIDE_INT = r'div'
t_MODULO     = r'mod'
t_EQUAL      = r'='
t_NEQUAL     = r'<>'
t_LT         = r'<'
t_GT         = r'>'
t_LE         = r'<='
t_GE         = r'>='
t_ASSIGN     = r':='

# Delimitadores
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_SEMICOLON  = r';'
t_COMMA      = r','
t_COLON      = r':'
t_DOT        = r'\.'
t_DOTDOT     = r'\.\.'

<<<<<<< HEAD
# Regular expression rules for complex tokens

def t_ABSOLUTE(t):
    r'absolute'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_CONST(t):
    r'const'
    return t

def t_DESTRUCTOR(t):    
    r'destructor'
    return t

def t_DOWNTO(t):
    r'downto'
    return t

def t_END(t):
    r'end'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_IF(t):
    r'if'
    return t

def t_INTEGER(t):  
    r'integer'
    return t

def t_REAL(t):
    r'real'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_IN(t):
    r'\bin\b'
    t.type = 'IN'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_LABEL(t):
    r'label'
    return t

def t_NIL(t):
    r'nil'
    return t

def t_OBJECT(t):
    r'object'
    return t    

def t_OR(t):
    r'or'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROGRAM(t):
    r'program'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_SHL(t):
    r'shl'
    return t

def t_STRING(t):
    r'string'
    return t

def t_TO(t):
    r'to'
    return t

def t_UNIT(t):
    r'unit'
    return t

def t_USES(t):
    r'uses'
    return t

def t_VIRTUAL(t):
    r'virtual'
    return t

def t_WITH(t):
    r'with'
    return t

def t_AND(t):
    r'and'
    return t

def t_ASM(t):
    r'asm'
    return t

def t_CASE(t):
    r'case'
    return t    

def t_CONSTRUCTOR(t):
    r'constructor'
    return t

def t_EXTERNAL(t):
    r'external'
    return t

def t_DO(t):
    r'do'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FILE(t):
    r'file'
    return t

def t_FORWARD(t):
    r'forward'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IMPLEMENTATION(t):
    r'implementation'
    return t

def t_INLINE(t):
    r'inline'
    return t

def t_INTERRUPT(t):
    r'interrupt'
    return t

def t_NOT(t):
    r'not'
    return t

def t_OFF(t):
    r'off'
    return t

def t_PACKED(t):
    r'packed'
    return t

def t_PROCEDURE(t):
    r'procedure'
    return t

def t_RECORD(t):
    r'record'
    return t

def t_SET(t):
    r'set'
    return t

def t_SHR(t):
    r'shr'
    return t

def t_THEN(t):
    r'then'
    return t

def t_TYPE(t):
    r'type'
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_XOR(t):
    r'xor'
=======
# Identificadores y palabras reservadas
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')  # Verifica si es una palabra reservada
>>>>>>> 14556444e3c4ee12d7c495af0295ceffdc1eaa8d
    return t

# Números
def t_REAL_CONST(t):
    r'\d+\.\d+([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_INTEGER_CONST(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Literales de cadena
def t_STRING_LITERAL(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]  # Remueve las comillas
    return t

# Comentarios { ... } y (* ... *)
def t_COMMENT(t):
    r'\{[^}]*\}|\(\*([^*]|\*+[^*)])*\*+\)'
    pass  # Ignorar comentarios

# Nueva línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados (espacios y tabulaciones)
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# Función de prueba del lexer (opcional)
def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Código para ejecutar el lexer (opcional)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = sys.argv[1]
    else:
        fin = '../examples/example2.pas'  # Ruta al archivo de ejemplo
    try:
        with open(fin, 'r') as f:
            data = f.read()
            lexer.input(data)
            for tok in lexer:
                print(tok)
    except FileNotFoundError:
        print(f"Error: El archivo '{fin}' no existe.")
