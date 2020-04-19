#linar - searching

#using while loop
pos = -1
print("enter your number that you want to find")
def search(list , n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1

    return False

list = [9,4,24,5,1,50]
n = int(input())

if search(list,n):
    print("found pos is ",pos+1)
else:
    print("not found")


#using for loop

def search2(arr ,x):
    for j in range(len(arr)):

        if arr[j] == x :
            return j
    return "not found"

arr = [0,4,1,44,23,2]
print("enter your number")
x = int(input())

print("num index -> ",search2(arr,x))



