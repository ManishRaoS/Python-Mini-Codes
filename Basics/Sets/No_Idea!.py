n, m = input().split()
arr = input().split()
a = input().split()
b = input().split()

arr = list(map(int, arr))
a = set(map(int, a))
b = set(map(int, b))
# n = int(n)
# m = int(m)

score = 0

for i in arr:
  if i in a:
    score = score + 1
  elif i in b:
    score = score - 1

print(score)