def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if n == 0:
        return True
    if not flowerbed:
        return False
    index = len(flowerbed)
    for i in range(index):
        if n==0:
            break
        if flowerbed[i] == 1:
            continue
        if index == 1 and flowerbed[i] == 0:
            n -= 1
            continue
        if i - 1 < 0:
            if flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue
        if i == index - 1:
            if flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue
        if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
    if n:
        return False
    else:
        return True



if __name__ == '__main__':
    # flowerbed = [0]
    # n = 1
    flowerbed =[0, 0, 1, 0, 0]
    n =1
    # flowerbed = [1, 0, 0, 0, 1]
    # n = 1
    res=canPlaceFlowers(flowerbed, n)
    print(res)