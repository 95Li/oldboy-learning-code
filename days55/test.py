def jisuan(a, b, c1,result):
    c2 = a + pow(b , 2) + pow(c1, 1.5)
    # result = c2 if abs(c1 - c2) < 0.001 else jisuan(a, b, c2)
    if (abs(c1-c2)<0.001):
        result=c2
    else:
        jisuan(a,b,c2,result)


if __name__ == '__main__':
    res=jisuan(1,3,5,3)
    print(res)