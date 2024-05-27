
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    print("Testing the functions:")
    print("3 + 4 =", add(3, 4))
    print("7 - 2 =", subtract(7, 2))
    print("5 * 6 =", multiply(5, 6))
    print("10 / 2 =", divide(10, 2))
