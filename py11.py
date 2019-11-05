def monj(c_cur, c_max):
    if c_cur > c_max:
        c_max = c_cur
    return c_max

def know_len1(monky):
    c_cur = 0
    c_max = 0
    for i in monky:
        if int(i) == 1:
            c_cur += 1
            c_max = monj(c_cur, c_max)
        else:
            c_cur = 0
    return c_max

def dec_to_bin(x):
    return int(bin(x)[2:])

if __name__ == '__main__':
    n = int(input())
    print(know_len1(str(dec_to_bin(n))))
