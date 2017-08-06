def ddd(price,colour,brand):   
	print('price:',price, # 这里后面加1个逗号，就可以把内容往下面写
		'colour:',colour,
		'brand:',brand)    #后面记得加括号结束

ddd(1000,'red','carmy')   #调用脚本




def aaa(price,colour='red',brand='fumeilai'):    # 这里也可以把colour和brand 定义好，这样在后面调用的时候就只要输入 price就可以打印出全部。但是定义的内容必须放在后面，也就是说brand 不能放在price前面，这样会报错。

	print('price:',price, # 这里后面加1个逗号，就可以把内容往下面写
		'colour:',colour,
		'brand:',brand)    #后面记得加括号结束

aaa(1231231)   #调用脚本
