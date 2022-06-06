def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    n, i, disappeared = len(nums), 0, list()

    # use cyclic sort to match 1-based indexes to corresponding integer
    while i < n:
        temp = nums[i]
        if nums[i] != i + 1 and temp != nums[temp - 1]:
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        else:
            i += 1

    # mismatched index indicates adsence of integer
    for i, num in enumerate(nums):
        if num != i + 1:
            disappeared += [i + 1]

    return disappeared
