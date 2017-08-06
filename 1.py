FEILONG = 10   # 全局定义，字母一般大写，顶格。
# 任何地方都可以取到这个全局变量。
a = None

def fun():
	a = FEILONG
		# 再打印出这个函数调用，就也是a+ 100 = 110。
		# 所以我们会看到 先显示一个 10  再显示 100
	return a+100


print(FEILONG)
print('1',a)
print(fun())
print('2',a)   #在这里可以打印X，但是打印不出来a,因为a 是fun()里面的局部变量。