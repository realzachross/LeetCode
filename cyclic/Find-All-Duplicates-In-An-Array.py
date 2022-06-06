def findDuplicates(self, nums: List[int]) -> List[int]:
    i, duplicates = 0, set()

    # match 1-indexed indices to corresponding values
    while i < len(nums):
        temp = nums[i]
        if nums[i] != i + 1 and temp != nums[temp - 1]:
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        # if two seperate indices have same value it is a duplicate
        elif temp == nums[temp - 1] and nums[i] != i + 1:
            duplicates.add(temp)
            i += 1
        else:
            i += 1

    return list(duplicates)
