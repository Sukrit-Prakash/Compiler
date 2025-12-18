INTEGER = 'INTEGER'
PLUS    = 'PLUS'
MINUS   = 'MINUS'
MUL     = 'MUL'
DIV     = 'DIV'
LPAREN  = 'LPAREN'
RPAREN  = 'RPAREN'
EOF     = 'EOF'
ID  = 'ID'
ASSIGN = 'ASSIGN'

# COMPARISON OPERATIORS
EQ = '=='
NEQ = '!='
LT = '<'
GT = '>'
LTE = '<='
GTE = '>='


class Token:
    def __init__(self,type,value):
        self.type=type
        self.value=value
        
    def __repr__(self):
        return f'Token({self.type}, {repr(self.value)})'

            
        
        