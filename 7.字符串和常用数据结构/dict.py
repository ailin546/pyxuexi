scores = {'爱林':100,'李新慧':60,'狄仁杰':76}
print(scores)
item1 = dict(one =1 ,two=2,three=3,four=4)
item2 = dict(zip(['a','b','c','d'],'1235'))
item3 = {num:num**2 for num in range(1,10)}
print(item1,item2,item3)
print(scores['李新慧'])
for key in scores:
    print(f'{key}:{scores[key]}')
scores['爱林'] = 150
scores['诸葛'] = 140
scores.update(冷面= 67,武则天=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
#get方法也是通过key获取对应的值但是可以设置默认值
print(scores.get('武则天'))
print(scores.get('武则天',60))
#删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('李新慧',60))
print(scores)
#清空字典
scores.clear()
print(scores)