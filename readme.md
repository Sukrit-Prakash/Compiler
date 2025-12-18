# MyLang: A Python-Based Custom Interpreter

A custom programming language implementation built from scratch in Python. This project demonstrates the core principles of language design, including lexical analysis, parsing, and interpretation.

## 🚀 Project Overview

MyLang is an interpreted language that supports arithmetic operations, variable assignments, unary operators, and memory management. It uses a **Recursive Descent Parser** and a **Tree-Walking Interpreter** to execute code in real-time.

## 🏗️ The Architecture (The Pipeline)

The language functions through a three-stage pipeline. Data flows sequentially from raw text to executable logic.

### 1. The Lexer (Lexical Analyzer)
**File:** `lexer.py`
* **Role:** The "Scanner." It reads the raw source code character by character.
* **Process:** It groups characters into meaningful chunks called **Tokens**.
* **Example:**
    * Input: `x = 5 + 10`
    * Output: `[ID('x'), ASSIGN, INTEGER(5), PLUS, INTEGER(10)]`
* **Key Features:** Handles multi-digit integers, ignores whitespace, and identifies keywords/identifiers.

### 2. The Parser (Syntax Analyzer)
**File:** `parser.py`
* **Role:** The "Grammar Police." It takes the list of tokens and validates them against the language's grammar rules.
* **Process:** It organizes tokens into a hierarchical structure called an **Abstract Syntax Tree (AST)**. It handles **Operator Precedence** (e.g., `*` happens before `+`) via a hierarchy of methods (`factor` → `term` → `expr`).
* **Example:**
    * The flat list `5 + 3 * 2` becomes a tree where `*` is deeper than `+`, ensuring `3*2` is calculated first.

### 3. The Interpreter (Runtime)
**File:** `interpreter.py`
* **Role:** The "Executor." It traverses the AST recursively.
* **Process:** It visits each node in the tree and performs the actual Python computation (addition, subtraction, memory storage).
* **Key Features:**
    * **Symbol Table:** A Python dictionary (`GLOBAL_MEMORY`) acts as the language's memory, storing variable values.

---

## 🛠️ Current Features

* **Arithmetic:** `+`, `-`, `*`, `/`
* **Parentheses:** `( )` for grouping expressions.
* **Unary Operators:** Negative numbers (e.g., `-5`, `--5`).
* **Variables:** Assignment (`x = 10`) and retrieval (`x + 5`).
* **Case Insensitivity:** (In logic handling)

## 🆚 How is this different from "Real" Compilers?

While MyLang follows the standard structure of a compiler, there are distinct differences between this educational project and industrial compilers like GCC (C++) or V8 (JavaScript).

| Feature | MyLang (Interpreter) | Real Compilers (e.g., C++, Java) |
| :--- | :--- | :--- |
| **Execution Mode** | **Interpreted.** The source code is read and executed line-by-line immediately. | **Compiled.** Source code is translated into Machine Code (0s and 1s) or Bytecode *before* it runs. |
| **Performance** | **Slower.** The overhead of "walking the tree" happens every time the code runs. | **Faster.** The CPU executes the optimized binary directly. |
| **Memory** | Uses Python's internal memory management. | Manages stack and heap memory manually (allocating addresses). |
| **Error Checking** | Runtime errors (crashes when it hits the bad line). | Static Analysis (finds errors *before* the code even runs). |
| **Intermediate Rep**| Uses an AST directly. | Uses **IR (Intermediate Representation)** (like LLVM IR) for optimization before machine code generation. |

## 🏃 How to Run

1.  Ensure all files (`tokens.py`, `lexer.py`, `parser.py`, `interpreter.py`, `main.py`) are in the same directory.
2.  Run the shell:
    ```bash
    python main.py
    ```
3.  Enter commands:
    ```text
    calc> a = 10
    10
    calc> b = 5
    5
    calc> result = a * b + (100 / 2)
    100.0
    ```

## 🔮 Future Roadmap

* [ ] Comparison Operators (`==`, `!=`, `<`, `>`)
* [ ] Control Flow (`If/Else` statements)
* [ ] Code Comments (`#`)
* [ ] Function Definitions (`def`)



after Finishing adding If/Else and Functions to your current Python interpreter first. Once the logic is solid, you can rewrite the backend to generate LLVM IR.