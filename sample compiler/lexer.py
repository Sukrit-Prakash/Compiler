        
# if __name__ == "__main__":
#     text = "12 + 3*(5 - 3 * 5)"
#     lexer = Lexer(text)

#     while True:
#         token = lexer.get_next_token()
#         print(token)
#         if token.type == EOF:
#             break

from tokens import * # Assuming tokens.py exists with INTEGER, PLUS, etc.

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.currentch = self.text[self.pos] if text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.currentch = self.text[self.pos]
        else:
            self.currentch = None
        
    def skip_whitespace(self):
        while self.currentch is not None and self.currentch.isspace():
            self.advance()
            
    def peek(self):
        peek_pos =self.pos +1
        if peek_pos > len(self.text)-1:
            return None
        return self.text[peek_pos]
            
    def _id(self):
        result =''
        while self.currentch is not None and self.currentch.isalnum():
            result += self.currentch
            self.advance()
        return Token(ID,result)
        
    def integer(self):
        result = ''
        while self.currentch is not None and self.currentch.isdigit():
            result += self.currentch
            self.advance()
        return int(result)
    
    def get_next_token(self):
        while self.currentch is not None:
            
            if self.currentch.isspace():
                self.skip_whitespace()
                continue

            if self.currentch.isdigit():
                return Token(INTEGER, self.integer())
            
            if self.currentch.isalpha():
                return self._id()
            
            if self.currentch == '!' and self.peek()=='=':
                self.advance()
                self.advance()
                return Token(NEQ,'!=')
            
            if self.currentch=='<':
                if self.peek()=='=':
                    self.advance()
                    self.advance()
                    return Token(LTE,'<=')
                else:
                    self.advance()
                    return Token(LT,'<')
            if self.currentch=='>':
                if self.peek()=='=':
                    self.advance()
                    self.advance()
                    return Token(GTE,'>=')
                else:
                    self.advance()
                    return Token(GT,'>')
            
            
            if self.currentch == '=':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    return Token(EQ,'==')
                else:
                    self.advance()
                    return Token(ASSIGN,'=')
            
            
            if self.currentch == '+':
                self.advance()
                return Token(PLUS, '+')
            
            if self.currentch == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.currentch == '*':
                self.advance()
                return Token(MUL, '*')

            if self.currentch == '/':
                self.advance()
                return Token(DIV, '/')

            if self.currentch == '(':
                self.advance()
                return Token(LPAREN, '(')
            
            if self.currentch == ')':
                self.advance()
                return Token(RPAREN, ')')
            
            # FIXED: Variable name mismatch (current_char -> currentch)
            raise Exception(f'Invalid character: {self.currentch}')
        
        return Token(EOF, None)
        
    #  first just write a compiler for ++ and - operations 
    # read blog and then make efficient for * and \ and then the brackets
    #  then improve the compiler as much as possible