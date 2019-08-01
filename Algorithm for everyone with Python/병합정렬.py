from sys import stdin
def merge_sort(mylist):
    if len(mylist) <= 1:
        return mylist
    half = len(mylist) // 2
    left_list = merge_sort(mylist[:half])
    right_list = merge_sort(mylist[half:])
    merged_list = []

    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            merged_list.append(right_list[0])
            right_list.pop(0)
        else:
            merged_list.append(left_list[0])
            left_list.pop(0)

    if len(left_list) > 0:
        merged_list += left_list
    if len(right_list) > 0:
        merged_list += right_list

    return merged_list

N = int(stdin.readline())
d = []
for i in range(N):
    ex = int(stdin.readline())
    d.append(ex)
d = merge_sort(d)
for i in d:
    print(i)
