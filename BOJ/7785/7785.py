log = dict()
for _ in range(int(input())):
    name, attended = input().split()
    log[name] = attended
answers = []
for key in log.keys():
    if log[key] == 'enter':
        answers.append(key)
answers.sort(reverse=True)
for answer in answers:
    print(answer)
