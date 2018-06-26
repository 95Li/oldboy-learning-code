def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    index = len(nums)
    nums = set(nums)
    for i in range(1, index + 1):
        if i not in nums:
            res.append(i)
    return res


if __name__ == '__main__':
    # nums=[4,3,2,7,8,2,3,1]
    nums = [3, 3, 4, 6, 5, 4]
    # nums=[1,1]
    res = findDisappearedNumbers(nums)
    print(res)
