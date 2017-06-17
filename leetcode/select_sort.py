from copy import deepcopy


def select_sort(data):
    temp = deepcopy(data)
    for i in range(len(temp)):
        for j in range(i,len(temp)):
            if temp[j]<temp[i]:
                temp[i],temp[j] = temp[j],temp[i]
    return temp


