white_row = 'WBWBWBWB'
black_row = 'BWBWBWBW'
mini = 100


def compare_board(x, y):
    global mini
    #흰색 칸 시작
    count = 0
    for i in range(8):
        row = board[y+i][x:x+8]
        if i%2==0:
            for a, b in zip(row, white_row):
                if a!=b: count += 1
        else:
            for a, b in zip(row, black_row):
                if a!=b: count += 1
    if count < mini: mini = count

    #검은 칸 시작
    count = 0
    for i in range(8):
        row = board[y+i][x:x+8]
        if i%2==0:
            for a, b in zip(row, black_row):
                if a!=b: count += 1
        else:
            for a, b in zip(row, white_row):
                if a!=b: count += 1
    if count < mini: mini = count

n, m = map(int, input().split())

#보드 입력받기
board = []
for i in range(n):
    board.append(input())

#보드 비교하기
for i in range(n-7):
    for j in range(m-7):
        compare_board(j, i)

print(mini)