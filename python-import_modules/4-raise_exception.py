def raise_exception():
    try:
        raise TypeError("This si exceptional")
    except TypeError as te:
        print("Exception has been raised")