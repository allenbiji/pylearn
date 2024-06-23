list=[1,7,1,3,4,3,2,6,3]

x,y=list[0],list[len(list)-1]
x,y=y,x
list[0],list[len(list)-1]=x,y

print(list)