def solution(arr):
    stack = []

    for x in arr:
        print(stack)
        if len(stack) == 0:
            for y in range(1, x+1):
                stack.append(y)
            if x != stack.pop():
                return False

        else:
            if x != stack.pop():
                return False

    return True

arr = [3, 1, 2]
print(solution(arr))