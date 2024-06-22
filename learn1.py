def ask():
    while True:
        try:

            a = int(input("enter an integer"))
            return a ** 2
        except TypeError:
            print("type error ")
            continue
        else:
            break
        finally:
            print('I am always here')


ask()

