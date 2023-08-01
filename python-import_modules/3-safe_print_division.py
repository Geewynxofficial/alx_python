def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # print("Division by zero is not allowed.")
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
if __name__ == "__main__":
  result = safe_print_division(10, 2)
  print(result)

  result = safe_print_division(10, 0)
  print(result)