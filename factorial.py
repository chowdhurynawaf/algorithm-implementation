print ("please enter your input")



def fact(value = int(input())) :
    if value == 0:
        return 1
    else:
        return value * fact(value - 1)

y = fact()

print(y)