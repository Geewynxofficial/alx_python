def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers.

  Args:
    matrix: The matrix to be printed.
  """

  if not matrix:
    print("")
    return

  for row in matrix:
    for col in row:
      print("{0:5d}".format(col), end=" ")
    print("{}")


