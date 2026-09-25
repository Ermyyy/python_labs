
def min_max(nums):
    if not nums:
        raise ValueError

    mn = nums[0]
    mx = nums[0]

    for x in nums:
        if x < mn:
            mn = x

        if x > mx:
            mx = x

    return mn, mx

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums):
    return sorted(set(nums))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat: list[list | tuple]) -> list:
    res = []
    for x in mat:
        if type(x) != list and type(x) != tuple:
            raise TypeError
        for el in x:
            res.append(el)
    return res

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))