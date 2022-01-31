# add function

def add(*arg):
    total = 0
    for i in arg:
        total += i
    return total


# ------------------------------------------------------------------------------------------------------
# length function

def length(arg):
    no_elements = 0
    for i in arg:
        no_elements += 1
    return no_elements


# count function

def count(a, arg):
    count = 0
    for i in arg:
        if i == a:
            count += 1
    print(count)


# maximum function

def maximum(arg):
    values = arg
    no_times = 0
    for i in values:
        for j in values:
            if i >= j:
                no_times += 1
            else:
                no_times = 0
                break
        if no_times == len(values):
            return i


# Minimum function
def minimum(arg):
    values = arg
    no_times = 0
    for i in values:
        for j in values:
            if i <= j:
                no_times += 1
            else:
                no_times = 0
                break
        if no_times == len(values):
            return i
