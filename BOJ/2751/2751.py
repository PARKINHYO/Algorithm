from sys import stdin
def shell_sort(random_list):
    h = 1
    while h < len(random_list):
        h = h * 3 + 1
    h = h // 3

    while h > 0:
        for i in range(h):
            start_index = i + h

            while start_index < len(random_list):
                temp = random_list[start_index]
                insert_index = start_index

                while insert_index > h - 1 and random_list[insert_index - h] > temp:
                    random_list[insert_index] = random_list[insert_index - h]
                    insert_index = insert_index - h

                random_list[insert_index] = temp
                start_index = start_index + h

        h = h // 3


N = int(stdin.readline())
d = []
for i in range(N):
    ex = int(stdin.readline())
    d.append(ex)
shell_sort(d)
for i in d:
    print(i)