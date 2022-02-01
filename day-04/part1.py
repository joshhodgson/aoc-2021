import re
lines = [str(f.strip("\n")) for f in open("input.txt")]
numbers = re.findall('\d+', lines[0])

boards = []
board = []
for l in lines[1:]:
    if l == "":
        if len(board) > 0:
            boards.append(board)
        board = []
    else:
        board.append(re.findall('\d+', l))
boards.append(board)


def checker(board, called):
    for i in range(len(board)):
        row = True
        column = True
        for j in range(len(board[i])):
            if board[i][j] not in called:
                row = False
            if board[j][i] not in called:
                column = False
        if row or column:
            allnums = sum(board, [])
            unused = [int(x) for x in allnums if x not in called]
            return (sum(unused))
    return False


called = []
answer = False
for n in numbers:
    called.append(n)
    for b in boards:
        if(checker(b, called)):
            print(n)
            print(checker(b, called))
            answer = checker(b, called) * int(n)
            break
    if(answer):
        break
print(answer)
