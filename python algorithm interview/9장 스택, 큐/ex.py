mylist = [1, 2, 3, 4, 5]

list2 = [x+1 for x in mylist]
mylist = map(lambda x: x+1 , mylist)

print(mylist)   