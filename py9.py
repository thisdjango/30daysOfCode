phoneBook = dict()
n = int(input())

for i in range(n):
    name, number = list(map(str, input().rstrip().split()))
    phoneBook[name] = number

for i in range(n):
    some_name = input()
    if some_name in phoneBook:
        st = str(some_name + '=' + phoneBook[some_name])
    else:
        st = 'Not found'
    print(st)
