x = 1
y = 2
z = 3

if x>y:
    print('x is false')  # 因为 x 不 大于 Y  所以这句是不会打印出来

if x<y:
    print('x is true')  # 因为X 小于 Y 这个条件是成立的，所以 这句会被打印出来。

if x < y < z:
    print('重复条件也可以输出，两个条件都成立')

if x <=y:
    print('X小于等于Y ，这个条件是对的')

# 符号有  < > <=  >=

if x == y:   # X 等于 Y  不是用"="， 而是用== , 一个等于号是 赋值。
    print('X是等于Y')

if x != y:   #运算符号前面加一个英文感叹号 ！ 就是表示不的意思，和mysql 里面一样。
    print('X不等于Y')