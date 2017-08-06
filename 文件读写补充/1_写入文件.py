text = 'This is my first test.\nThis is next line.\nThis is last line.'
#  \n 表示换行

my_file = open('my_file1.txt','w')  # 第一次用open 创建 my_file1.txt 文件。w 表示可读可写，r表示只读
my_file.write(text)  #text 内容为上面第一行的内容
my_file.close()