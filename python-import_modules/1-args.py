import sys

if __name__ == "__main__":
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # The first element in sys.argv is the script name itself

    # Print the number of arguments
    # print("Number of argument(s): {}".format(num_args))

    if num_args > 0:
        # Print the list of arguments
        print("Arguments: {}".format(num_args))

        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        # No arguments were passed
        print(":")

