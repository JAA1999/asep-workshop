def do_something():
    pass


def example_function(param_1, param_2):
    if param_1:
        for i in range(param_2):
            do_something()
    else:
        new_var = param_2/2
        for i in range(new_var):
            do_something()
    return 0

example_function(1, 10)
# example_function(False, 10)
# example_function(0, 9)