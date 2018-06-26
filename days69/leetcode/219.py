def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    from collections import Counter
    count_dic = Counter(nums)
    res_dic = {}
    diff=[]
    for i in range(len(nums)):
        v = nums[i]
        if count_dic[v] > 1:
            if v in res_dic:
                for index in res_dic[v]:
                       diff.append(i - index)
                res_dic[v].append(i)
            res_dic[v] = [i]

    if diff and min(diff)<=k:
        return True
    return False




# nums = [1,2,3,1]
# k = 3
# nums = [1,0,1,1]
# k = 1
# nums = [1,2,3,1,2,3]
# k = 2
#
nums=[99,99]
k=2
res=containsNearbyDuplicate(nums, k)
print(res)
