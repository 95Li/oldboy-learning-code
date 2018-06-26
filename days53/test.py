code="""
global x
x=0
y=2
"""
global_dic={'x':100000}
local_dic={}
exec(code,global_dic,local_dic)

print('global_dic:',global_dic)
print('local_dic',local_dic)