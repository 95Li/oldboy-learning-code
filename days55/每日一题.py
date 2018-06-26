def get_res(n):
    list1=[i for i in range(n)]
    res_list = []
    for i in range(n):
        res = map(lambda x: x * i, list1)
        res_list.append(list(res))
    return res_list


res = get_res(5)
print(res)
