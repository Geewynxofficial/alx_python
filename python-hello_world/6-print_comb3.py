for i in range(0,10):
    for j in range(i+1, 10):
        print("{:01d}{:01d}".format(i,j), end="," if i < 8 else "\n")
print()
