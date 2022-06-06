def findDuplicateCyclicSort(self, nums: List[int]) -> int:
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


def findDuplicateCycleDetect(self, nums: List[int]) -> int:
    fast = slow = 0
    # detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break

    # cycle start is equidistant from head of graph and meeting node
    slow = 0
    while fast != slow:
        fast = nums[fast]
        slow = nums[slow]

    return fast
