n = int(input("Enter number of elements in the set A"))
set_a = input("Enter elements of set A").split()
set_a = set(set_a)

n_com = int(input("Enter the number of inputs"))
comlist = []

for i in range(n_com * 2):
    com_set = input("Enter command followed by the set B").split()
    comlist.append(com_set)

for ind, command in enumerate(comlist):
    if command[0] == "intersection_update":
        set_a.intersection_update(comlist[ind + 1])
    elif command[0] == "symmetric_difference_update":
        set_a.symmetric_difference_update(comlist[ind + 1])
    elif command[0] == "difference_update":
        set_a.difference_update(comlist[ind + 1])
    elif command[0] == "update":
        set_a.update(comlist[ind + 1])

print(sum(set(map(int, set_a))))
