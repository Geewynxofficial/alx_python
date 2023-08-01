def safe_print_division(a, b):
    try:
        result = a / b
        a = 10
        b = 2
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None
    else:
        print("Inside result: {}".format(result))
    finally:
        return result

# result = safe_print_division(a, b)
