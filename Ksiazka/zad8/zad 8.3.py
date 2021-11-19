#safe division function

def safe_division(num1, num2):
    try:
        return num1/num2
    except Exception:
        print("Division by 0!")
        return 0

print(safe_division(1,0))