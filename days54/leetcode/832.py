def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    if not A:
        return A
    indexs = len(A)
    for i in range(indexs):
        A[i]=list(reversed(A[i]))
        index = len(A[i])
        for j in range(index):
            x = 0 if A[i][j] == 1 else 1
            A[i][j] = x
    return A

if __name__ == '__main__':
    A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    # A=[[1,1,0],[1,0,1],[0,0,0]]
    res=flipAndInvertImage(A)
    print(res)