set_a = input().split()
n = int(input())

oper_list = []

for i in range(n):
    oper_input = input().split()
    oper_list.append(oper_input)

final_list = []
for i in oper_list:
    if set(i).intersection(set(set_a)) == set(i) and len(set(i).intersection(set(set_a))) < len(set_a):
        final_list.append("True")
    else:
        final_list.append("False")

if "False" in final_list:
    print("False")
else:
    print("True")