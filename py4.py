if __name__ == '__main__':
    N = int(input())
    answer = 'Weird' if N%2 or not N%2 and 21 > N > 5 else 'Not Weird'
    print(answer)
