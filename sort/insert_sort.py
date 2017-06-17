def insert_sort(data):
    """O(n^2) time and O(1) space"""
    for i in range(len(data)):
        for j in range(i,0,-1):
            if data[j] < data[j - 1]:
                data[j],data[j -1] = data[j - 1],data[j]
    return data
