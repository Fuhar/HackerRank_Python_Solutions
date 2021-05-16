if __name__ == '__main__':
    N = int(input())

    cmd_list = list()
    lst = []
    p = ''

    for i in range(N):
        cmd_list.append(input())

    for j in cmd_list:

        if j[0] == 'i':
            t = j.split()
            lst.insert(int(t[1]),int(t[2]))

        elif j[0] == 'a':
            t = j.split()
            lst.append(int(t[1]))

        elif j[0] == 's':
            lst.sort()

        elif j[0] == 'r':

            if j[:3] == 'rem':
                t = j.split()
                lst.remove(int(t[1]))

            else:
                lst.reverse()

        else:

            if j[:2] == 'po':
                a = lst.pop()

            else:
                print(lst)
