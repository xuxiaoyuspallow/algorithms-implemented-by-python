
def bubble_sort(data):
    # O(n^2) time and O(1) space
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    return data


def improved_bubble_sort(data):
    for i in range(len(data)):
        swap_flag = False
        for j in range(len(data)-1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap_flag = True
        if not swap_flag:
            return data
