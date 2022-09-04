while True:
    numbers = input().split()
    D, N = numbers
    res = ""

    if D == '0' and N == '0' or not D.isnumeric() or not N.isnumeric():
        break
    else:
        for i in N:
            if i != D:
                res = res + i
        if res == "" or int(res) == 0:
            res = "0"
    res = int(res)
    print(res)
