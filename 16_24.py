def solve(arr, k):
    seen = set()
    pairs = []
    for x in arr:
        if k - x in seen:
            pairs.append((x, k - x))
        seen.add(x)
    return pairs


print(solve([1, 3, 5, 7, 2, 4], 6))
