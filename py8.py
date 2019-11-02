if __name__ == '__main__':
    n = int(input())

    arr = list(map(str, input().rstrip().split()))
    r = ' '.join(arr[::-1])
    print(r)
