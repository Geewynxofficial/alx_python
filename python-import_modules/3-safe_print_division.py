def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        result = None
    else:
        print("Inside result: {}".format(result))
    finally:
        print("{} / {} = {}".format(a, b))