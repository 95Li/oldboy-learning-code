def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    ads_num=abs(num)
    if (ads_num < 7 and ads_num >0 )or num==0:
        return str(num)

    qu, re = divmod(ads_num, 7)
    re = str(re)
    re = convertToBase7(qu) +re
    if num<0:
        re='-'+re
    return re

# num=30
# num=-7
# num=-8
# num=-1
# res=convertToBase7(num)
# print(res)


if __name__ == '__main__':
    qu=-8//7
    re=-8%7
    print(qu)
    print(re)
    qu, re = divmod(-8, 7)
    print(qu)
    print(re)