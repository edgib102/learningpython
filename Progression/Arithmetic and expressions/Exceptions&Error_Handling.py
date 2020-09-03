x = 0
y = 0
def error():
    print(x / y) # runs expetion as you cant divide zero
    print("ran function")
    quit()


try:
    error()
except ZeroDivisionError as DivError:
    print()
    print(DivError)
    print()
    while True:

        inputvalx = input("enter x value: ")
        inputvaly = input("enter y value: ")
        

        try:
            x = int(inputvalx)
            y = int(inputvaly)
            error()
        except ValueError as ValError:
            print()
            print (ValError)
            print()
        except ZeroDivisionError as DivError:
            print()
            print(DivError)
            print()

#divides by 0, then reasigns the ints to something else with exeption handling



