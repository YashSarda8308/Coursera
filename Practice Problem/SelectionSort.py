import time
import random
l = [random.randrange(1,10000)]
print(l)
def selectionsort(lst,reverse=False):
    print("Unsorted list --> ",lst)
    # if reverse==True:
    #     m = max
    # else:
    #     m = min
    # for i in range(len(lst)-1):
    #     min_value = m(lst[i:])
        
    #     index = lst.index(min_value,i)# search from index i or last min value
    #     if lst[i]!=lst[index]:
    #         lst[i],lst[index] = lst[index],lst[i]
    
    min_value = lst[0]
    for i in range(len(lst)-1):
        min_value = lst[i]
        for j in range(i+1,len(lst)):
            if lst[j]<min_value:
                min_value = lst[j]
        index = lst.index(lst[j])
        lst[j],lst[index] = lst[index],lst[j]
        print(lst,min_value,sep=' ===> ')

    print("\nSorted list --> ",lst)
    return lst
selectionsort([0,5,0,3,6,8,5,9,1])
t = time.perf_counter()
print(t)