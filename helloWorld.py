list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

list.append(12) #在列表末尾添加新的对象
list.count(786)  #统计某个元素在列表中出现的次数
print(list)
print(list.count(786))
# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置，索引从0开始
# list.insert(index, obj) 将对象插入列表
# list.pop() 移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
# list.remove(obj) 移除列表中某个值的第一个匹配项
# list.reverse() 反向列表中元素，倒转
# list.sort([func]) 对原列表进行排序
