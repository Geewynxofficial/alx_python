import sys

def print_arguments():
  """
  Prints the number of and the list of its arguments.
  """

  number_of_arguments = len(sys.argv)
  if number_of_arguments == 0:
    print("No arguments")
  else:
    print(f"Number of arguments: {number_of_arguments}")
    for i in range(1, number_of_arguments + 1):
      print(f"Argument {i}: {sys.argv[i - 1]}")


if __name__ == "__main__":
  print_arguments()
