from collections import Counter

n = input("Size of group")
b = input("Enter room list").split()

k = Counter(b)

d = dict(k)

print(min(d, key=lambda k: d[k]))