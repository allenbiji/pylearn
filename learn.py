name=[("Ajith",7),('Aleena',8),('Job',4)]

def hours(name):
    largest=0
    for x,y in name:
        if y > largest:
            largest=y
            long=x
        else:
            pass
    return f'{long} worked the longest with {largest} hours'

b=hours(name)
print(b)