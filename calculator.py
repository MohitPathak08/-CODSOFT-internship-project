def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculator():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    print("Simple Calculator (type 'quit' to exit)\n")

    while True:
        try:
            user_input = input("Enter expression (e.g. 3 + 5): ").strip()
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break

            for op in operations:
                if op in user_input:
                    parts = user_input.split(op, 1)
                    a, b = float(parts[0].strip()), float(parts[1].strip())
                    result = operations[op](a, b)
                    print(f"= {result}\n")
                    break
            else:
                print("Invalid expression. Use +, -, *, /\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception:
            print("Invalid input. Try again.\n")

if __name__ == "__main__":
    calculator()
