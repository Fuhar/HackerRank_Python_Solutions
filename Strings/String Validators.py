if __name__ == '__main__':
    s = input()

    an, a, d, l, u = [],[],[],[],[]

    for i in s:
        an.append(i.isalnum())
        a.append(i.isalpha())
        d.append(i.isdigit())
        l.append(i.islower())
        u.append(i.isupper())

    print(any(an))
    print(any(a))
    print(any(d))
    print(any(l))
    print(any(u))
