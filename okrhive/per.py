# permu = [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [
#     3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]

# permuatations = [1, 2, 3, 4]


# def permute(nums):
#     res = []

#     def backtrack(i):
#         # if we fixed all positions, record permutation
#         if i == len(nums):
#             res.append(nums[:])  # copy
#             return

#         for j in range(i, len(nums)):
#             # place nums[j] at position i
#             nums[i], nums[j] = nums[j], nums[i]
#             backtrack(i+2)
#             # backtrack
#             nums[i], nums[j] = nums[j], nums[i]

#     backtrack(0)
#     return res


# # example
# arr = [1, 2, 3, 4]
# print(permute(arr))
# -> [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]


p = "poovarasan"

longest = ""

for i in range(len(p)):
    seen = set()
    current = ""

    for j in range(i, len(p)):
        if p[j] in seen:
            break

        seen.add(p[j])
        current += p[j]

    if len(current) > len(longest):
        longest = current

print("Longest substring:", longest)
print("Length:", len(longest))
