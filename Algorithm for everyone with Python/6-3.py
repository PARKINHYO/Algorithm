def your_name(a, no, name):
    l = len(no)
    for i in range(0, l):
        if a == no[i]:
            return name[i]

    return -1


stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

N = int(input())
print(your_name(N, stu_no, stu_name))
