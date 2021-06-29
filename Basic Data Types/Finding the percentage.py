if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum_m = 0
    for marks in student_marks[query_name]:
        sum_m += marks
    avg = "{:.2f}".format(sum_m/3)
    print(avg)
