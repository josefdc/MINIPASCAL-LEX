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
    'integer': 'INTEGER',
    'real': 'REAL',
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

# Identificadores y palabras reservadas
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')  # Verifica si es una palabra reservada
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
