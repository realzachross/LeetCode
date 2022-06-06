def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    removals, end = 0, float('-inf')
    for s, e in sorted(intervals, key=lambda i: i[1]):
        if s >= end:
            end = e
        else:
            removals += 1
    return removals
