def select_sort(data):
    """O(n^2) time and O(1) space"""
    for i in range(len(data)):
        for j in range(i + 1,len(data)):
            if data[j] < data[i]:
                data[i], data[j] = data[j],data[i]
    return data

