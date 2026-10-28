#!/usr/bin/env python3
"""
Simple Calculator Program
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    print("=== Simple Calculator ===")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        try:
            choice = input("\nEnter choice (1-5): ").strip()
            
            if choice == '5':
                print("Thank you for using the calculator!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please try again.")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                except ValueError as e:
                    print(f"Error: {e}")
            
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except EOFError:
            print("\nThank you for using the calculator!")
            break
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main()
