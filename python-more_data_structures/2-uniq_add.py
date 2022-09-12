#!/usr/bin/python3
def uniq_add(my_list=[]):
    counts = {}
    for i in my_list:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1

    result = [k for k, v in counts.items() if v == 1]
    return sum(result)
