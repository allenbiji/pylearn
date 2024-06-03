def check_even_list(num_list):
    even=[]
    for number in num_list:
        if number % 2 == 0:
            even.append(f'{number} is True')
        else:
            pass
    return even

a= check_even_list([1,2,4])
print(a)