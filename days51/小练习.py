def test(l1):
    # l2=[]
    # for l in l1:
    #     if l not in l2:
    #         l2.append(l)

    l2=list(set(l1))
    l2.sort(key=l1.index)

    return l2


l1 = [11, 2, 3, 22, 2, 4, 11, 3]
res=test(l1)
print(res)