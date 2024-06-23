l1=['amma','allen',1001,2000,2002]

for i in l1:
    if type(i)==int:
        a=str(i)[::-1]
        if int(a)==i:
            print("palindrome")
        else:
            print("not palindrome")
    else:
        a=i[::-1]
        if a==i:
            print("palindrome")
        else:
            print("not palindrome")
