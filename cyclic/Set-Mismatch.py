def findErrorNums(self, nums: List[int]) -> List[int]:
    i, n, res = 0, len(nums), set()
    while i < n:
        temp = nums[i]
        if temp <= n and temp != i + 1 and nums[temp - 1] != temp:
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        elif nums[temp - 1] == temp and temp != i + 1:
            res.add(temp)
            i += 1
        else:
            i += 1

    res = list(res)
    for i in range(n):
        if nums[i] != i + 1:
            res += [i + 1]
            return res
    return None
