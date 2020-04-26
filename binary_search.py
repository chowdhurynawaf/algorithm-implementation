pos = -1

def binarySearch(list , number):

    lower = 0
    upper = len(list)-1

    while lower <= upper :
        mid = (lower+upper) // 2

        if list[mid] == number:
            globals()['pos'] = mid
            return True

        else:
            if list[mid] < number:
                lower = mid+1
            else:
                upper = mid-1
    return False



list = [2,3,4,9 ,10,11,12]

number = 4

if binarySearch(list,number):
    print("found at ", pos+1)
else:
    print("not found")

