import sys
input = sys.stdin.readline 


N = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())

# 원하는 예산 합이 총 예산보다 작으면 바로 원하는 예산들 중 최대 값 출력
if sum(budgets) < total_budget:
    print(max(budgets))
    exit(0)
    
budgets.sort()
left, right = 0, N
while left < right:
    mid = (left + right) // 2
    first, second = False, False
    
    """
    총예산에서 {중간 값 이전 예산들의 합 + (중간값 x 절반개수)}을 뺀 값이 
    0보다 크거나 작은지에따라 left, right 포인터를 조정.
    딱 맞아떨어지면 해당 예산을 출력하고 바로 종료.
    """
    if (total_budget - (sum(budgets[:mid]) + len(budgets[mid:])*budgets[mid])) > 0:
        left = mid+1
        first = True
    elif (total_budget - (sum(budgets[:mid]) + len(budgets[mid:])*budgets[mid])) < 0:
        right = mid
        second = True
    else:
        print(budgets[mid])
        break

"""
위의 while문에서 if에서 종료됐는지 elif에서 종료됐는지에 따라 
총예산에 가까워질 때까지 예산을 1씩 더하거나 뺌.
"""
if first:
    cur = budgets[mid]
    while sum(budgets[:mid+1]) + len(budgets[mid+1:])*cur < total_budget:
        cur += 1
        
    """
    종료하면 sum(budgets[:mid+1]) + len(budgets[mid+1:])*cur > total_budget 상태로 종료되므로,
    cur에서 1빼주고 출력
    """
    print(cur-1)
if second:
    cur = budgets[mid]
    while sum(budgets[:mid]) + len(budgets[mid:])*cur > total_budget:
        cur -= 1
    print(cur)

