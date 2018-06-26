def hasAlternatingBits(n):
    n=bin(n)[2::]
    for i  in range(1,len(n)):
        if n[i]==n[i-1]:
           return False

    return True



if __name__ == '__main__':
    n=10
    res=hasAlternatingBits(n)
    print(res)