def arrayPairSum(nums):
    if not nums:
        return None
    nums = sorted(nums)
    nums1 = nums[0::2]
    nums2 = nums[1::2]
    list_num = zip(nums1,nums2)
    sum = 0
    for a in list_num:
        sum += min(a)
    print(sum)


# nums = [1, 4, 3, 2]
nums=[1, 4, 3, 2,5,8]
arrayPairSum(nums)
