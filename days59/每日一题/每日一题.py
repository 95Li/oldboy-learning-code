"""
编写Python脚本，分析xx.log文件，按域名统计访问次数

xx.log文件内容如下：
https://www.sogo.com/ale.html
https://www.qq.com/3asd.html

https://www.sogo.com/teoans.html
https://www.bilibili.com/2
https://www.sogo.com/asd_sa.html
https://y.qq.com/

https://www.bilibili.com/1
https://dig.chouti.com/
https://www.bilibili.com/imd.html
https://www.bilibili.com/

输出：
4 www.bilibili.com
3 www.sogo.com
1 www.qq.com

1 y.qq.com

1 dig.chouti.com
"""

import re
from collections import Counter
def count_log(path):
    res=dict()
    with open(path,'r',encoding='utf-8' )as f:
        data=f.read()
    res = dict()
    data=re.findall('//(.*?)/',data)
    '''
    第一种：
    '''

    #     for line in data:
    #         if line in res:
    #             res[line]+=1
    #         else:
    #             res[line]=1
    # lis=sorted(res,key=lambda x:res[x],reverse=True)
    # for k in lis:
    #     print('%s ,  %s' %(res[k],k))
    '''
    第二种：
    '''
    dic=Counter(data)
    print(dic)
    ret=sorted(dic.items(),key=lambda x :x[1],reverse=True)
    for k,v in ret:
        print(v,k)

if __name__ == '__main__':
    res=count_log(r'xx.log')



