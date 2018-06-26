def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    disticit_list = list(set(nums))
    # print(disticit_list)
    # print(disticit_list == nums)
    if sorted(disticit_list) == sorted(nums):
        return False
    else:
        return True

num=[1,2,3,4]
res=containsDuplicate(num)
print(res)