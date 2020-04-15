n = int(input("Enter number of elements in the set"))
s = set(map(int, input("Enter set elements").split()))
n_com = int(input("Enter number of commands"))

commands = []
for i in range(n_com):
  command = input("Enter command").split()
  commands.append(command)

for i in commands:
  if len(i) == 1:
    try:
      s.pop()
      print(s)
    except KeyError:
      continue
  elif len(i) > 1:
    if i[0] == "remove":
      try:
        s.remove(int(i[1]))
      except KeyError:
        continue
    else:
      s.discard(int(i[1]))

print(len(s))
print(sum(s))
