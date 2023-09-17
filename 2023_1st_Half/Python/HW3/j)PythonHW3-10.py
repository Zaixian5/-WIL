# 3-10. 하노이의 탑 문제에서 원판을 옮기는 과정을 표시하는 함수 만들기

def hanoi1(n, src, tmp, dst):
    stack = [('hanoi1', n, src, tmp, dst)]
    while len(stack) > 0:
        task = stack.pop()
        func = task[0]
        if func == 'hanoi1':
            n = task[1]
            src = task[2]
            tmp = task[3]
            dst = task[4]
            if n > 1:
                stack.append(('hanoi1', n-1, tmp, src, dst))
                stack.append(('print', src, '==>', dst))
                stack.append(('hanoi1', n-1, src, dst, tmp))
            else:  # n == 1
                stack.append(('print', src, '==>', dst))
        elif func == 'print':
            src = task[1]
            arrow = task[2]
            dst = task[3]
            print(src, arrow, dst)

# 문제10 테스트1
hanoi1(3, 'A', 'B', 'C') # 3개의 원판을 A에서 C로 옮기는 과정

print("")
# 문제10 테스트2
hanoi1(4, 'A', 'B', 'C') # 4개의 원판을 A에서 C로 옮기는 과정