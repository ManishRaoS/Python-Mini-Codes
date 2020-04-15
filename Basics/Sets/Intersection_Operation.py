n1 = int(input("Enter number of students in set 1"))
set_1 = input("Enter student roll numbers").split()
set_1 = set(set_1)

n2 = int(input("Enter number of students in set 2"))
set_2 = input("Enter student roll numbers").split()
set_2 = set(set_2)

print(len(set_1.intersection(set_2)))