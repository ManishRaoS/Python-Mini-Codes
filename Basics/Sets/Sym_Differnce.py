# Symmetric distance
m = input("here") # numer of integers in the first set
m_inp = input("first").split() # first line of integers
n = input("here") # number of integers in the second set
n_inp = input("second").split() # second line of integers

s1 = set(list(map(int, m_inp)))
s2 = set(list(map(int, n_inp)))

# print(list(s1^s2))

diff_list = s1.difference(s2).union(s2.difference(s1))

for i in sorted(diff_list):
    print(i)
