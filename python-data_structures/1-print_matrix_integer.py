def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join([str(col).rjust(5) for col in row]))
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
            print("")



