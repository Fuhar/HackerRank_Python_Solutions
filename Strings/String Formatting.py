def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1,number+1):
        o = oct(i)[2:]
        h = hex(i).upper()[2:]
        b = bin(i)[2:]
        print(str(i).rjust(width), o.rjust(width), h.rjust(width), b.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
