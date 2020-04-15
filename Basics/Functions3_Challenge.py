def func_0(arr_1, arr_2):
    return [min(value) for value in zip(arr_1, arr_2)]


def func_1(arr_1, arr_2):
    a = sorted(arr_1).copy()
    b = sorted(arr_2).copy()
    return list(func_0(a, b))


def func_2(my_string):
    result = "->".join(my_string[i:i + 1] for i in range(0, len(my_string)))
    return result

