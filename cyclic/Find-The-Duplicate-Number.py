def findDuplicate(self, nums: List[int]) -> int:
    i = 0

    # cyclically sort list
    while i < len(nums):
        if nums[i] != i + 1:
            temp = nums[i]
            # if duplicated numbers at different indices
            if temp == nums[temp - 1]:
                return temp
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        else:
            i += 1

    return None
