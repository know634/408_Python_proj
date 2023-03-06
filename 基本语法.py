# -- coding: utf-8 --

# 新建变量
a = 1
b = 2
c = 3
# 新建数组
d = [1, 2, 3]
# 新建字典
e = {'a': 1, 'b': 2, 'c': 3}
# 新建元组
f = (1, 2, 3)
# 新建集合
g = {1, 2, 3}
# 新建字符串
h = '123'
# 新建布尔值
i = True
# 新建空值
j = None

# 对数组进行操作，访问，修改，删除，添加，切片，循环，判断，排序，反转，长度，最大值，最小值，求和，求平均值
# 访问
print("访问数组d的第一个元素：", d[0])
# 修改
d[0] = 4
print("修改数组d的第一个元素为4：", d)
# 删除
del d[0]
print("删除数组d的第一个元素：", d)
# 添加
d.append(5)
print("添加元素5到数组d的末尾：", d)
# 切片
print("切片数组d的第二个元素到第三个元素：", d[1:3])
# 循环
for i in d:
    print("循环数组d的每个元素：", i)
# 判断
if 5 in d:
    print("判断数组d中是否存在元素5：", True)
else:
    print("判断数组d中是否存在元素5：", False)
# 排序
d.sort()
print("对数组d进行排序：", d)
# 反转
d.reverse()
print("对数组d进行反转：", d)
# 长度
print("数组d的长度：", len(d))
# 最大值
print("数组d的最大值：", max(d))
# 最小值
print("数组d的最小值：", min(d))
# 求和
print("数组d的求和：", sum(d))
# 求平均值
print("数组d的求平均值：", sum(d) / len(d))

# 对字典进行操作，访问，修改，删除，添加，循环，判断，长度，清空
# 访问
print("访问字典e的第一个元素：", e['a'])
# 修改
e['a'] = 4
print("修改字典e的第一个元素为4：", e)
# 删除
del e['a']
print("删除字典e的第一个元素：", e)
# 添加
e['d'] = 5
print("添加元素5到字典e的末尾：", e)
# 循环
for i in e:
    print("循环字典e的每个元素：", i)
# 判断
if 'a' in e:
    print("判断字典e中是否存在元素a：", True)
else:
    print("判断字典e中是否存在元素a：", False)
# 长度
print("字典e的长度：", len(e))
# 清空
e.clear()
print("清空字典e：", e)

# 对元组进行操作，访问，切片，循环，判断，长度，最大值，最小值，求和，求平均值
# 访问
print("访问元组f的第一个元素：", f[0])
# 切片
print("切片元组f的第二个元素到第三个元素：", f[1:3])
# 循环
for i in f:
    print("循环元组f的每个元素：", i)
# 判断
if 5 in f:
    print("判断元组f中是否存在元素5：", True)
else:
    print("判断元组f中是否存在元素5：", False)
# 长度
print("元组f的长度：", len(f))
# 最大值
print("元组f的最大值：", max(f))
# 最小值
print("元组f的最小值：", min(f))
# 求和
print("元组f的求和：", sum(f))
# 求平均值
print("元组f的求平均值：", sum(f) / len(f))