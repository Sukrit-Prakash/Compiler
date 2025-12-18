   # --- THE PIPELINE ---
            
            # Step 1: Lexical Analysis
            # Converts "3 + 5" into [INTEGER(3), PLUS, INTEGER(5)]
            lexer = Lexer(text)