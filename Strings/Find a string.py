def count_substring(string, sub_string):
    ls = len(sub_string)
    l = len(string)
    c = 0
    for i in range(l-ls+1):
        if string[i:i+ls] == sub_string:
            c += 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
