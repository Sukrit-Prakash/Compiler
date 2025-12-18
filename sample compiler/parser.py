from tokens import *
from lexer import *

# --- AST NODES ---
class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
class UnaryOp(AST):
    def __init__(self,op,expr):
        self.op=op
        self.expr = expr
        
class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        
class Var(AST):
    def __init__(self,token):
        self.token =token
        self.value = token.value
        
class Assign(AST):
    def __init__(self,left,op,right):
        self.left = left
        self.token = self.op =op
        self.right = right

# --- PARSER ---
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self):
        raise Exception('Invalid Syntax')
    
    def eat(self, token_type):
        # compare the current token type with the passed token type
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
            
    def factor(self):
       
        token = self.current_token
        
        if token.type in (PLUS,MINUS):
            self.eat(token.type)
            node =self.factor()
            node = UnaryOp(op=token,expr=node)
            return node
        """Parse a single number."""
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token) 
        
        elif token.type == ID:
            self.eat(ID)
            return Var(token)
            
        self.error()

    def term(self):
        """Parse * and / (Higher Priority)"""
        node = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node
   
#    ASSIGN def __init__(self,left,op,right):

    def assignment(self):
        left = Var(self.current_token)
        self.eat(ID)
        token =self.current_token
        self.eat(ASSIGN)
        right =self.expr()
        return Assign(left,token,right)
        
        
    def expr(self):
        """Parse + and - (Lower Priority)"""
        # FIXED: Call term(), not eat() directly
        node = self.term() 
        
        # FIXED: Added colon and fixed logic loop
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)
            
            # FIXED: Create a BinOp node
            node = BinOp(left=node, op=token, right=self.term())
        
        return node
        
    def parse(self):
        # current_val = self.current_token.value
        if self.current_token.type ==ID and self.lexer.text.find('=')!=-1:
            print("reched here")
            return self.assignment()
        # pass
        return self.expr()