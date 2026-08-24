def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error"

def calculator():
    while True:
        print("\n1.Add 2.Sub 3.Mul 4.Div 5.Exit")
        choice = input("Choice: ")
        if choice == '5': break
        if choice not in ('1', '2', '3', '4'): continue
        try:
            n1 = float(input("Num 1: ")); n2 = float(input("Num 2: "))
            if choice == '1': print(add(n1, n2))
            elif choice == '2': print(subtract(n1, n2))
            elif choice == '3': print(multiply(n1, n2))
            elif choice == '4': print(divide(n1, n2))
        except ValueError: print("Invalid number")

if __name__ == "__main__": calculator()
