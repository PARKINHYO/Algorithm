from collections import defaultdict


def solution(k, score):

    score_diff = []
    score_diff_dic = defaultdict(int)

    for i in range(len(score) - 1):
        score_diff.append(score[i] - score[i + 1])
        score_diff_dic[score[i] - score[i + 1]] += 1

    keys = []
    for key, val in score_diff_dic.items():
        if val >= k:
            keys.append(key)

    del_index = []
    for i in range(len(score_diff)):
        if score_diff[i] in keys:
            del_index.append(i)

    del_index_set = set(del_index)
    for i in del_index:
        del_index_set.add(i+1)

    return len(score)-len(del_index_set)


# k = 3
# score = [24, 22, 20, 10, 5, 3, 2, 1]

k = 2
score = [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]

solution(k, score)
