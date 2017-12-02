def is_triangle():
    print('삼각형의 길이를 입력하시오.')
    a = input(' ')
    b = input(' ')
    c = input(' ')

    if not (a.isnumeric() and b.isnumeric() and c.isnumeric()):
        print('숫자를 입력해주세요.')
        return is_triangle()

    a,b,c = float(a), float(b), float(c)

    if not a > 0 and b > 0 and c > 0:
        print('길이를 양수로 입력하세요.')
        return is_triangle()

    tmp = [a,b,c]
    maximum = max(tmp)
    tmp.remove(maximum)

    if maximum < tmp[0] + tmp[1]:
        print('예')
    else:
        print('아니요')

if __name__ == '__main__':
    is_triangle()