# Import the components we created in the other files
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

global_scope = {}

def main():
    print("Welcome to YourLang! (Type 'exit' or 'quit' to stop)")
    
    while True:
        try:
            # 1. Get Input
            # We use 'calc> ' as a prompt to show the program is ready
            text = input('calc> ')
            
            # Check for exit commands
            if text.strip().lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            
            # If the user just hits enter, skip this loop iteration
            if not text:
                continue

            # --- THE PIPELINE ---
            
            # Step 1: Lexical Analysis
            # Converts "3 + 5" into [INTEGER(3), PLUS, INTEGER(5)]
            lexer = Lexer(text)
            print(lexer)
            
            # Step 2: Parsing
            # Converts tokens into an AST Tree: BinOp(Num(3), +, Num(5))
            parser = Parser(lexer)
            print(parser)
            
            # Step 3: Interpretation
            # Walks the tree and calculates the result: 8
            interpreter = Interpreter(parser)
            interpreter.GLOBAL_MEMORY = global_scope
            
            result = interpreter.interpret()
            
            # Output the result
            print(result)

        except Exception as e:
            # This catches errors like "Invalid Syntax" or "Invalid Character"
            # so the program doesn't crash entirely.
            print(f"Error: {e}")

if __name__ == '__main__':
    main()