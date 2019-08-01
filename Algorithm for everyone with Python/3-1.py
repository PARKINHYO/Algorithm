def match_machine(a):
    l = len(a)
    for i in range(0, l):
       for j in range(i+1, l):
           print(a[i] + "-" + a[j])

list = ["Tom", "Jerry", "Mike"]
match_machine(list)