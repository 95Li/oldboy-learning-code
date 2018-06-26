def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    # sum = 0
    # op = []
    # indexs = len(ops)
    # for index in range(indexs):
    #
    #     if ops[index] == '+':
    #         scord = op[-1] + op[-2]
    #         op.append(scord)
    #         sum += scord
    #     elif ops[index] == 'D':
    #         scord = op[-1] * 2
    #         op.append(scord)
    #         sum += scord
    #     elif ops[index] == 'C':
    #         scord = op.pop()
    #         sum -= scord
    #     else:
    #         scord = int(ops[index])
    #         op.append(scord)
    #         sum += scord
    # return sum

    op = []
    indexs = len(ops)
    for index in range(indexs):

        if ops[index] == '+':
            scord = op[-1] + op[-2]
            op.append(scord)

        elif ops[index] == 'D':
            scord = op[-1] * 2
            op.append(scord)

        elif ops[index] == 'C':
            scord = op.pop()

        else:
            scord = int(ops[index])
            op.append(scord)

    return sum(op)

# list=[]
list=0
# list=["5","-2","4","C","D","9","+","+"]
# list = ["5", "2", "C", "D", "+"]
res = calPoints(list)
print(res)


# if __name__ == '__main__':
#     a='-3'
#     print(a.isdigit())