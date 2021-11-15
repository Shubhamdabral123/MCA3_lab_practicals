# KM MINAKSHI 20712152  MCA 3C GEHU Dehradun

N = 4


def transpose(A, B):

    for i in range(N):
        for j in range(N):
            B[i][j] = A[j][i]


A = [[11, 11, 11, 11],
     [12, 12, 12, 12],
     [13, 13, 13, 13],
     [14, 14, 14, 14]]


B = A[:][:]

transpose(A, B)

print("Result matrix is")
for i in range(N):
    for j in range(N):
        print(B[i][j], " ", end='')
    print()
