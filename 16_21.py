def solve(a, b):
    asum, bsum = map(sum, [a, b])
    aset, bset = map(set, [a, b])
    diff = (asum - bsum) // 2
    for x in aset:
        wanted = x - diff
        if wanted in bset:
            return (x, wanted)


assert solve([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]) == (1, 3)
