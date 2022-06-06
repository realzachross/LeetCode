def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    f = s = 0
    res = []

    while f < len(firstList) and s < len(secondList):

        # detect overlap
        if firstList[f][0] <= secondList[s][1] and secondList[s][0] <= firstList[f][1]:
            res += [[max(firstList[f][0], secondList[s][0]),
                     min(firstList[f][1], secondList[s][1])]]

        # increment the pointer(s)
        if firstList[f][1] < secondList[s][1]:
            f += 1
        elif firstList[f][1] > secondList[s][1]:
            s += 1
        else:
            s, f = s + 1, f + 1

    return res
