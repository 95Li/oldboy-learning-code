from collections import Counter
c = Counter()
dic=Counter('programming')

for ch in 'programming':
    c[ch] = c[ch] + 1

print(dic)
print("===========")
print(c)

'''
输出：
Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
===========
Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
'''
