    def peakElement(self, arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low

#=====================================================

    arr.insert(0, float('-inf'))
    arr.append(float('-inf'))
    start = 1
    end = len(arr) - 1
    for i in range(start, end):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return 1
        else:
            continue
    return 0