def triangleSP():
    a = int(input())
    b = int(input())
    c = lambda x, y: x * y
    d = lambda x, y: (x + y) * 2
    clist = [c(a, b), d(a, b)]
    for i, arg in enumerate(clist):
        print(i, arg)
    print(clist)
    print((' '.join(str(e) for e in clist)))

triangleSP()