# import sys

# if __name__ == "__main__":
#     # Get the number of arguments
#     num_args = len(sys.argv) - 1  # The first element in sys.argv is the script name itself

#     # Print the number of arguments
#     # print("{} argument:".format(num_args))

#     if num_args > 0:
#         # Print the list of arguments
#         print("{} arguments:".format(num_args))

#         for i, arg in enumerate(sys.argv[1:], start=1):
#             print("{}: {}".format(i, arg))
#     else:
#         # No arguments were passed
#         print("{} arguments.".format(num_args))



import sys

def print_arguments():
    argv = sys.argv[1:]
    num_args = len(argv)

    print(f"{num_args} argument{'s' if num_args != 1 else ''}{':' if num_args > 0 else '.'}")

    if num_args > 0:
        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")

if _name_ == "_main_":
    print_arguments()
