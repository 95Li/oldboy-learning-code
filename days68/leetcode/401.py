from itertools import combinations, permutations


# l = ['0', '0', '0', '0', '1']
#
# res_l = combinations(l, 1)
# print(list(res_l))
# str_list = [''.join(r) for r in set(res_l)]
# res=['%s:%s' % (int(i[0:3],2), str(int(i[3:],2)).rjust(2,'0')) for i in str_list]
# print(res)

def readBinaryWatch(num):
    """
    :type num: int
    :rtype: List[str]
    """
    l = ['0', '0', '0', '0']
    r = ['0', '0', '0', '0', '0', '0']
    for i in range(num):
        l[i] = '1'
    res_l = set(permutations(l, 10))

    print(res_l)
    print(len(res_l))
    str_list = [''.join(r) for r in res_l]
    res_list = ['%s:%02d' % (int(i[0:4], 2), int(i[4:], 2)) for i in str_list if int(i[0:4], 2) <= 11]
    print(len(res_list))
    return res_list


num = 2
res = readBinaryWatch(num)
print(res)
