def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Finally block executed.")