def this_function_has_a_bug(param):
    if param >= 0:
        example_var = 1
        example_var_2 = 2
        another_function()
        return 10/param
    else:
        print(f'{param} is must be greater than 0')


def another_function():
    for i in range(3):
        print(f'{i}th loop')

try:
    print(f'{int(this_function_has_a_bug(0.238))} is the answer to life')
except Exception:
    print('We should really implement real error handling')
