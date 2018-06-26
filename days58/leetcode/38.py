def get_val(a):
    res=''
    count=0
    val=a[0]
    for i in list(a):
        if i==val:
            count+=1
        else:
            res=res+str(count)+val
            val=i
            count = 1
    res = res + str(count) + val
    return res


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """

    res='1'
    for i in range(n-1):
        res=get_val(res)
    return res

if __name__ == '__main__':
    # n=1
    n=6
    res=countAndSay(n)
    print(res)

