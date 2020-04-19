def quicksort(sequence):
    length = len(sequence)
    if length <= 1 :
        return  sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []



    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    #return quicksort(items_lower)+[pivot]+ quicksort(items_greater) #low to high
    return quicksort(items_greater)+[pivot]+quicksort(items_lower) #high to low


print(quicksort([5,54,2,4,67,8,3,2]))

