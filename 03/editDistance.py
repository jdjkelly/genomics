def editDistanceRecursive(x,y):
    ''' Recursively determine the edit distance between two strings '''
    # If the length of X is 0, then the distance between them is the length of Y
    if len(x) == 0:
        return len(y)
    # Similarly, if the length of Y is 0, then the distance between them is the length of X
    if len(y) == 0:
        return len(x)
    # Find the difference between the last characater of X and Y. If they're different, the difference is 1, otherwise they are the same and it's 0
    delt = 1 if x[-1] != y[-1] else 0
    # Find the minimum
    return min(editDistanceRecursive(x[:-1], y[:-1]) + delt,
               editDistanceRecursive(x[:-1], y) + 1,
               editDistanceRecursive(x, y[:-1]) + 1)

def editDistanceDynamic(x,y):
    '''
        Dynamically determine the edit distance between two strings. We do this by matrix math.

              e G C T A T A
             ______________
          e  |0|1|2|3|4|5|6|
          G  |1|0|2|3|4|5|6|
          C  |2|1|0|1|2|3|4|
          G  |3|2|1|?|2|3|4|
          T  |4|3|2|1|2|2|3|
          A  |5|4|3|2|1|2|2|
          T  |6|5|4|3|2|1|2|

          Each cell corresponds to the edit distance between the strings, ie.
          (4,4 compares GCTA and GCGT, which is an edit distance of 2)

          What is the edit distance of (5,5 GCTAT and GCGTA)? It's the minimum
          of:
            - Distance between two equal length prefixes (4,4 GCTA and GCGT),
              plus the delta of the last character (T and A) 
              - = 1
            - Distance between prefix of the first string and the full second
              string, plus 1 for the missing character (3,4 GCT and GCGT)
              - = 2
            - Distance between the full first string and a prefix of the second
              string, plus 1 for the missing character (4,3 GCTA and GCG)
              - = 2

          1,1 is always going to be 0 since that compares empty strings 
          1,N is always going to be an empty string vs. a different string, so N is
          always y co-ord 
          N,1 is always going to be an emptry string vs.
          a different string, so N is always x co-ord

          Final distance is the bottom right

          With this method, for any given A, B pair of strings, we're storing
          the value - meaning recalculation never occurs, unlike the recusrive version
    '''
    D = []                          # Initialize array
    for i in range(len(x)+1):        
        D.append([0]*(len(y)+1))    # For each column, create a row of 0s
    for i in range(len(x)+1):
        D[i][0] = i                 # For each row in the first column, set the value to equal the row count
    for i in range(len(y)+1):
        D[0][i] = i                 # For each column in the first row, set the value to equal the column count

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1         # Find the value of [x][y-1] + 1 (shorter version of second string + 1)
            distVer = D[i-1][j] + 1         # Find the value of [x-1][y] + 1 (shorter version of first string + 1)
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]      # Find the value of [x-1][y-1] + delta (equal length prefixes)
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag) # Find the min of all above value
    return D[-1][-1]



x = 'shake spea'
y = 'Shakespear'
print(editDistanceRecursive(x,y))
print(editDistanceDynamic(x,y))

alphabet = ['A', 'C', 'G', 'T']
score = [[0, 4, 2, 4, 8], \
         [4, 0, 4, 2, 8], \
         [2, 4, 0, 4, 8], \
         [4, 2, 3, 0, 8], \
         [8, 8, 8, 8, 8]]

def globalAlignment(x, y):
    D = []                          
    for i in range(len(x)+1):        
        D.append([0]*(len(y)+1))   
    for i in range(len(x)+1):
        D[i][0] = D[i-1][0] + score[alphabet.index(x[i-1])][-1]
    for i in range(len(y)+1):
        D[0][i] = D[0][i-1] + score[-1][alphabet.index(y[i-1])]
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + score[-1][alphabet.index(y[j-1])]
            distVer = D[i-1][j] + score[alphabet.index(x[j-1])][-1]
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
            D[i][j] = min(distHor, distVer, distDiag) # Find the min of all above value
    return D[-1][-1]

x = 'TACCAGATTACA'
y = 'TACCAGATTACA'
print(globalAlignment(x,y))

