# for循环，给定了一个区间
# 变量等于1 做什么，等于2 做什么，等于3 做什么。

example_list = [1,2,3,4,6,7,12,543,876,12,3,5]
# 中括号 里面的表示 list

for i in example_list: # i 是example_list 里面的一个值。
    print(i)  # 打印出 example_list 里面的所有值，每个。

    print('inner of for') # 每打印一个 i 就打印一个 inner of for
# 全选内容后按 TAB 可以缩进一个TAB， 也就是4个空格。
print('end')  # 打印完 example_list 里面的所有，才打印end。

# 从上面的可以看出，四个空格（1个TAB）是很重要的。python 结构是非常重要的。

for x in range(1,10): # range 是电脑自动生成的迭代器，range(1,10) 表示 1-9(不包括10，而是1，2，3，4，5，6，7，8，9)
    print(x)


for u in range(1,10,2): # 后面的2 表示进位 1 3 5 7 9
    # 如果把2改成5的话，那么就是 1, 6
    print(u)