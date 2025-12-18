from tokens import *

class NodeVisitor: 
    def visit(self, node):
        # This dynamic method dispatch allows us to call 'visit_BinOp' 
        # or 'visit_Num' depending on the node type
        method_name = 'visit_' + type(node).__name__
        
        # method_name = 'visit_' + type(node).__name__ -> returns 'visit_Assign'.
        
        visitor = getattr(self, method_name, self.generic_visit)
        
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser
        self.GLOBAL_MEMORY = {}

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == LT:
            return self.visit(node.left) <  self.visit(node.right)
        elif node.op.type == GT:
            return self.visit(node.left) > self.visit(node.right)
        elif node.op.type == LTE:
            return self.visit(node.left) <= self.visit(node.right)
        elif node.op.type == GTE:
            return self.visit(node.left) >= self.visit(node.right)
        elif node.op.type == EQ:
            return self.visit(node.left) == self.visit(node.right)
        elif node.op.type == NEQ:
            return self.visit(node.left) != self.visit(node.right)
        
    def visit_UnaryOp(self,node):
        if node.op.type == MINUS:
            return -1 * self.visit(node.expr)
        elif node.op.type == PLUS:
            return self.visit(node.expr)
            
    def visit_Assign(self,node):
        var_name =node.left.value
        value =self.visit(node.right)
        self.GLOBAL_MEMORY[var_name]=value
        return value
    
    #  toretrive dta from variable
    def visit_Var(self,node):
        var_name = node.value
        val =self.GLOBAL_MEMORY.get(var_name)
        if val is None:
            raise Exception(f"NameError: name '{var_name}' is not defined")
        return val
    
    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)