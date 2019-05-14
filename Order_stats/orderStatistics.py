#Find the smallest number
def smallest(order):
    min=order[0]
    min2=order[1]
    for i in order:
        if i<min:
            min,i=i,min
            if (i<min2):
                min2,i=i,min2
    return min, min2

def sort(swap_list):
    for list in range(len(swap_list)-1,0,-1):
        for i in range(list):
            if swap_list[i]>swap_list[i+1]:
                swap_list[i],swap_list[i+1]=swap_list[i+1],swap_list[i]
    print(swap_list)

print(smallest([1,6,3,9,8,5,0,-2]))

given_list=[1,3,4,6,0,5,2]
sort(given_list)
