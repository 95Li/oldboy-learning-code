import math


def constructRectangle(area):
    """
    :type area: int
    :rtype: List[int]
    """
    dim=int(math.sqrt(area))
    while dim>0:
        if area%dim==0:
            return [int(area/dim),int(dim)]
        dim-=1

if __name__ == '__main__':
    area=2
    res=constructRectangle(area)
    print(res)