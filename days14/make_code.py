
# def make_code(n):
#     pass
#
# w=30
# print('[%-d%]')

#
# # =========实现打印进度条函数==========
# import sys
# import time
#
#
# def progress(percent, width=50):
#     if percent >= 1:
#         percent = 1
#     show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
#     print('\r%s %d%%' % (show_str, int(100 * percent)), file=sys.stdout, flush=True, end='')
#

# # =========应用==========
# data_size = 1025
# recv_size = 0
# while recv_size < data_size:
#     time.sleep(0.1)  # 模拟数据的传输延迟
#     recv_size += 1024  # 每次收1024
#
#     percent = recv_size / data_size  # 接收的比例
#     progress(percent, width=70)  # 进度条的宽度70


import random
import time
def pri_Progress(pro):
    w=60
    figure=('[%%-%ds]'%w)%('#'*int(60*pro))
    pro=100*pro
    print('\r%s %d%%'%(figure,pro),end=' ')

data_size = 1025
load_size = 0
while not load_size>data_size:
    pro=load_size/data_size
    time.sleep(0.1)
    pri_Progress(pro)
    num=random.randint(20,50)
    load_size+=num
    if load_size>data_size:
        load_size=data_size




