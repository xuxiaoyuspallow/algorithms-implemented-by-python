
def merge(nums1,nums2):
    """
    """
    if not nums1:
        return nums2
    elif not nums2:
        return nums1
    res = []
    while nums1 or nums2:
        if nums1 and nums2:
            small = nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0)
            res.append(small)
        elif nums1:
            res.append(nums1.pop(0))
        elif nums2:
            res.append(nums2.pop(0))
    return res


def merge_sort(data):
    if len(data) <= 1:
        return data
    if len(data) == 2:
        if data[0] > data[1]:
            data[0], data[1] = data[1], data[0]
        return data
    mid = len(data) // 2
    return merge(merge_sort(data[:mid]), merge_sort(data[mid:]))


data = [1,9,2,3,5,4,7,7,11,3,23]

print(merge_sort(data))
    