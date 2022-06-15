import numpy as np

def getRatio(s, t):

    rows = len(s)+1

    cols = len(t)+1

    distance = np.zeros((rows,cols),dtype = int)

    for i in range(1, rows):

        for k in range(1,cols):

            distance[i][0] = i

            distance[0][k] = k

    for col in range(1, cols):

        for row in range(1, rows):

            if s[row-1] == t[col-1]:

                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0

            else:

                cost = 2

            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions

                                 distance[row][col-1] + 1,          # Cost of insertions

                                 distance[row-1][col-1] + cost)     # Cost of substitutions

    return ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
