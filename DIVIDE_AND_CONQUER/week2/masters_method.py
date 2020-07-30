A = int(input())
B = int(input())
D = int(input())

if A ==B**D:
    print("The running time of the algorithm is")
    print("n^",D,"log n")

elif A <B**D:
    print("The running time of the algorithm is")
    print("n^",D)
else:
    print("The running time of the algorithm is")
    print("n^Log",D)
