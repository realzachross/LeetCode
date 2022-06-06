def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    f = s = 0
    res = []

    while f < len(firstList) and s < len(secondList):
        f_start, s_start = firstList[f][0], secondList[s][0]
        f_end, s_end = firstList[f][1], secondList[s][1]

        # detect overlap
        if f_start <= s_end and s_start <= f_end:
            res += [[max(f_start, s_start), min(f_end, s_end)]]

        # increment the pointer(s)
        if f_end < s_end:
            f += 1
        else:
            s += 1

    return res
