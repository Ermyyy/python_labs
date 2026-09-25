# def transpose(mat: list[list[float | int]]) -> list[list]:
#     if not mat:
#         return []

#     for x in mat:
#         if len(x) != len(mat[0]):
#             raise ValueError

#     res = []

#     for j in range(len(mat[0])):
#         newmat = []
#         for i in range(len(mat)):
#             newmat.append(mat[i][j])
#         res.append(newmat)
#     return res
# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))

# def row_sums(mat: list[list[float | int]]) -> list[float]:
#     for st in mat:
#         if len(st) != len(mat[0]):
#             raise ValueError
#     res = []
#     for st in mat:
#         res.append(sum(st))
#     return res

# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))

def col_sums(mat: list[list[float | int]]) -> list[float]:
    for x in mat:
        if len(x) != len(mat[0]):
            raise ValueError
    res = []
    for j in range(len(mat[0])):
        s = 0
        for i in range(len(mat)):
            s += mat[i][j]
        res.append(s)
    return res

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))

