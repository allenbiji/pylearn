def myfunc(*args,**kwargs):
    return ('I need {} {}'.format(args[2],kwargs['food']))

b=myfunc(20,30,40,food='apple',fav='cow')
print(b)