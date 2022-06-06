def firstMissingPositive(self, nums: List[int]) -> int:
    i, n = 0, len(nums)

    # perform cyclic sort to match index to corresponding value if possible
    while i < n:
        temp = nums[i]
        if nums[i] != i + 1 and nums[i] <= n and nums[i] > 0 and nums[temp - 1] != temp:
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        else:
            i += 1

    # first mismatch corresponds to first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    else:
        return n + 1
