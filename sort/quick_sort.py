def quick_sort(lists):
    # 快速排序
    if len(lists) <= 1:
        return lists
    left = 0
    right = len(lists) - 1
    key = lists[left]
    low = []
    high = []
    for i,v in enumerate(lists):
        if i == left:
            continue
        if v <= key:
            low.append(v)
        else:
            high.append(v)
    lists[right] = key
    lists = quick_sort(low) + [lists[left]] + quick_sort(high)
    return lists
