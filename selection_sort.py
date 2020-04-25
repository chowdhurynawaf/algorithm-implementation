def selectionSort(list):
    for i in range(len(list)):
        minpos = i

        for j in range(i,len(list)):
            if list[j] < list[minpos]:
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

        print(list)


list = [5, 6 , 0 , -1 , 87 , 45]
selectionSort(list)
print("\nffinal sorted array"," : ", list)


