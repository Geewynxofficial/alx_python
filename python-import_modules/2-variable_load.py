def load_variable():
    with open("variable_load_2.py", "r") as f:
        source = f.read()

    # Import the variable a from the source code
    a = eval(source)["a"]

    return a


if __name__ == "__main__":
    print(load_variable())
