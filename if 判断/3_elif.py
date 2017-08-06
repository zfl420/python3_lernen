x = -1121
y = 2
z = 3
if x>1:
    print('X大于1')
elif x<1:  #满足这个条件，只会打印这个。
    print('X小于1')
elif x<-10: #也满足这个条件，但是由于上面一个条件已经满足，所以跳出循环。
    print('X小于-10')
else:
    print('X等于1')

print('循环已经结束')



