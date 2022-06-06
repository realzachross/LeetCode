def findKthPositive(self, arr: List[int], k: int) -> int:
    k -= arr[0] - 1
    if k <= 0:
        return arr[0] + k - 1
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 1:
            k -= arr[i] - arr[i - 1] - 1
            if k <= 0:
                return arr[i] + k - 1
    return arr[-1] + k
