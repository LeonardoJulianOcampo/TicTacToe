diagonal = []
board = [[j+1 + i*3 for j in range(3) ] for i in range(3)] 

for i in range(3):
	diagonal.append(board[i][-i-1])

print(board)

print(board[0][-1])
print(board[1][-2])
print(board[2][-3])

print(diagonal)
