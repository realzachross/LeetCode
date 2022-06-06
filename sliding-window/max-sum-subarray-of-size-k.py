def maxSub(nums, k):
    start, stop = 0, k - 1
    res = temp = sum(nums[start: stop + 1])
    start += 1
    stop += 1
    while stop < len(nums):
        temp = temp + nums[stop] - nums[start - 1]
        res = max((res, temp))
        print(res)
        start += 1
        stop += 1
    return res


print(maxSub([3, 4, 6, -5, 1, 1, 0, 9], 6))
