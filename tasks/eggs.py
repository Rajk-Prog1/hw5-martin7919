def eggs_solution(breaks):
    for i in range(1,101):
        if breaks(i):
            return i - 1
    return 100
