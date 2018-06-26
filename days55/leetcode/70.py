def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # if n==0 or n==1:
    #     return n
    # res=climbStairs(n-1)+climbStairs(n-2)
    # return res
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    n=4
    res=climbStairs(n)
    print(res)
