file = open('my_file1.txt','r') # r 表示读取，把文件存到了file而不是文件里面的内容

content = file.readlines()  # 读取的my_file1里面的内容并且保存为 content

# read是读取文件内全部内容， readline 是读取第一行， readlines是读取所有行(包括换行符号)

print(content)   #打印出 conten

