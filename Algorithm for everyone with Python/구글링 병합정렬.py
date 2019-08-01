from sys import stdin

def mergeSort(A):
    if len(A)<=1:
        return A
    left=mergeSort(A[:len(A)//2])
    right=mergeSort(A[len(A)//2:])
    i,j,k = 0, 0, 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            A[k]=left[i]
            i+=1
        else :
            A[k]=right[j]
            j+=1
        k+=1
    if i==len(left): #left의 원소를 모두 사용 했으나 right가 남아 있을 경우 #
        while j<len(right):
            A[k]=right[j]
            j+=1
            k+=1
    elif j==len(right): #right의 원소를 모두 사용 했으나 left가 남아 있을 경우 #
        while i<len(left):
            A[k]=left[i]
            i+=1
            k+=1
    return A

N = int(stdin.readline())
d = []
for i in range(N):
    ex = int(stdin.readline())
    d.append(ex)
d2 = mergeSort(d)
for i in d2:
    print(i)
