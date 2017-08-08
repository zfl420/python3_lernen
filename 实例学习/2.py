globvar = 0

def set_globvar_to_one():
	global globvar    # 需要用global修饰一下globvar
	globvar = 1

def print_globvar():
    print(globvar)     # 如果要读globbar的值的话不需要用global修饰

set_globvar_to_one()
print_globvar()       # 输出 1