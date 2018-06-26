
def func(m):
    n=dict.copy(m)
    for k,v in n.items():
        m[k+2] = v+2


m = {1: 2, 3: 4}
l = m  # 浅拷贝
l[9] = 10
func(l)
m[7] = 8


print("l:", l)
print("m:", m)
