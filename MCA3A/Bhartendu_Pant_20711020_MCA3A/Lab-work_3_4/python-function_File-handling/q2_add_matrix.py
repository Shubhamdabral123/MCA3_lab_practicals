


def sum1(M1,M2):

    sum = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

    for i in range(len(M1)):
        for j in range(len(M1[0])):
            sum[i][j] = M1[i][j] + M2[i][j]


    for num in sum:
        print(num)
        


# first matrix
M1 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]

# second matrix
M2 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]

sum1(M1,M2)
