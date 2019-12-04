def count_stair_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)

if __name__ == "__main__":
    for n, value in enumerate([1, 1 ,2 ,3 ,5 ,8 ,13 ,21 ,34 ,55]):
        res = count_stair_ways(n)
        assert res == value, "exp:%d got:%d for n = %d" % (value, res, n)