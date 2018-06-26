from collections import Counter
def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    candies_dic=Counter(candies)
    num=len(candies)/2+len(candies)%2
    types=len(candies_dic)
    return int(num) if num<=types else types


if __name__ == '__main__':
    # candies = [1, 1, 2, 2, 3, 3]
    candies = [1, 1, 2, 3]
    res=distributeCandies(candies)
    print(res)