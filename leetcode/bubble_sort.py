from copy import deepcopy


# O(n^2) in the best situation
def bubble_sort(data):
    temp = deepcopy(data)  # do not change outside data
    for i in range(len(temp)):
        for j in range(len(temp)-1):
            if temp[j]>temp[j+1]:
                temp[j],temp[j+1] = temp[j+1],temp[j]
    return temp


# O(n) in the best situation
def improved_bubble_sort(data):
    temp = deepcopy(data)  # do not change outside data
    for i in range(len(temp)):
        swap_flag = False
        for j in range(len(temp)-1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                swap_flag = True
        if not swap_flag:
            return temp



