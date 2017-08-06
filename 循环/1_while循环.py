# while 循环，当条件满足就做什么

condition = 1
while condition < 10:  #当condition小于10
    print(condition)    # 打印 condition，也就是10
    condition = condition + 1   #重新定义condition = 1（上面定义的) + 1 ,结果是2
    # 上面打印了1次 是2 ，再加1 等于3  一直到10就不满足 condition < 10 的条件 就会停止这个循环。


# while

while True:  # 如果条件一直满足，那他就会一直循环，俗称死循环。
    print("I'm True")