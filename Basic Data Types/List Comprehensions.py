if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = []
    for p in range(x+1):
        for q in range(y+1):
            for r in  range(z+1):
                if p + q + r != n:
                    lst.append([p, q, r])
    print(lst)
