import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def multiply_matrix(arr1, arr2):
    answer = []
    for idx1 in range(len(arr1)):
        row = []
        for idx2 in range(len(arr2[0])):
            tmp = 0
            for idx3 in range(len(arr1[0])):
                tmp += arr1[idx1][idx3] % 1000 \
                    * arr2[idx3][idx2] % 1000
                tmp = tmp % 1000
            row.append(tmp)
        answer.append(row)
    return answer


def solution(exp):
    global matrix
    if(exp == 1):
        return matrix
    
    """
    분할 정복해서 계산수를 줄인다. 
    1승 x 1승, 2승 x 2승, 4승 x 4승 형태로 계산한다..
    """
    t = solution(exp//2)
    
    # 인자로 넘어온 행렬을 곱하는 함수
    t = multiply_matrix(t, t)
    
    """
    맨처음 b가 홀수로 주어졌을 때 만약 5라고 하면, 
    solution(5) -> solution(2) -> solution(1)순으로 호출되고 
    solution(5)에서 위의 t가 4제곱근이므로 만약 처음에 홀수였다면 1제곱근을 한번 더 곱해준다. 
    """
    if(exp % 2 != 0):
        t = multiply_matrix(t, matrix)
    return t


n, b = map(int, input().rstrip().split())
matrix = []
for i in range(n):
    matrix.append([*map(lambda x: x % 1000,
                        map(int, input().split(" ")))])

# solution함수에 인자로 지수를 넣어주면 정답 반환.
for m in solution(b):
    print(*m)

