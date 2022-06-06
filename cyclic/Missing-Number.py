def missingNumber(self, nums: List[int]) -> int:
    n, i = len(nums), 0

    # use cyclic sort on list
    while i < n:
        if nums[i] < n and nums[i] != i:
            temp = nums[i]
            nums[i] = nums[nums[i]]
            nums[temp] = temp
        else:
            i += 1

    # find the mismatched index: this corresponds to missing num
    for i in range(n):
        if nums[i] != i:
            return i

    # if no mismatch, num is n
    return n
