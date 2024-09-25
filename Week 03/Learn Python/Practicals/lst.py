# Given two lists of integers, write a program that generates a list of tuples where each
# tuple contains corresponding elements from the two lists.
# The resulting list should only include tuples where the first element
# is greater than the second.
# lst = [
#     [1, 2, 3],
#     [4, 5,6],
#     [7, 8, 9]]
# # new_lst = []
# # for i in lst:
# #     new_lst.extend(i)
# # print(new_lst)
# diagonal_lst = [lst[i][l] for i in range(len(lst)) for l in range(len(lst[i])) if l == i]
# # print(diagonal_lst)
# lst = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# name = [i[0] for i in lst if i[1]>30]
# print(name)
# lst = [[i*j for i in range(1,11)]for j in range(1,6)]
# print(lst)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def cum_sum(lst):
    cum_lst = []
    for i in range(len(lst)):
        if cum_lst:
            cum_lst.append(lst[i] - lst[i-1])
        else:
            cum_lst.append(lst[i])
    return cum_lst
print(cum_sum(lst))


# k = 0
# for i in lst:
#     if i != 0:
#         lst[k] = i
#         k += 1
# while k < len(lst):
#     lst[k] = 0
#     k+=1
# print(lst)
# rev_lst = []
# length = len(lst) - 1
# for i in range(length,-1,-1):
#     rev_lst.append(lst[i])
# print(rev_lst)
