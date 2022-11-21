def nagasai(m):
    sign = '-' if m<0 else ''
    m = abs(m)
    if m < 3:
        return str(m)
    s = ''
    while m != 0:
        s = str(m%3) + s
        m = m//3
    return sign+s
m=int(input())
print(nagasai(m))