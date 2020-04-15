n_testcase = int(input("Enter number of test cases"))

oper_list = []
for i in range(n_testcase*4):
    oper_input = input("Enter number of elements in set A followed by elements of set and same for B").split()
    oper_list.append(oper_input)

set_a_list = []
for i in range(1, len(oper_list), 4):
    set_a_list.append(oper_list[i])

set_b_list = []
for i in range(3, len(oper_list), 4):
    set_b_list.append(oper_list[i])


for i, j in zip(set_a_list, set_b_list):
    if len(set(i).intersection(j)) == len(set(i)):
        print("True")
    else:
        print("False")
