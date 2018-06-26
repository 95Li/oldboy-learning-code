def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    num1_list = list(num1)
    num2_list = list(num2)

    sum1 = 0
    sum2 = 0
    for n in num1_list:
        sum1 = (sum1 * 10) + int(n)
    for n in num2_list:
        sum2 = sum2 * 10 +int(n)

    return str(sum1 + sum2)

res=addStrings('124','124')
print(res)