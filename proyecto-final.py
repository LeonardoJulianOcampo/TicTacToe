import os
from random import randrange

############################################################ Definición de funciones ############################################################


def initializeBoard():    #Carga los elementos por defecto en el tablero (las coordenadas)
     board = [[j+1 + i*3 for j in range(3) ] for i in range(3)] 
     return board


def print_divider():
    for i in range(25):    #Genera el patron de caracteres de la primera fila del tablero
        if i % 8 == 0:
            if i == 24:
                print("+")
            else:
                print("+",end="")
        else:
            print("-", end="")


def print_coordinates(board, row): # Toma como datos los elementos de la lista board y la fila actual para hacer la impresion de cada elemento en el tablero.
    
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[row][0],board[row][1],board[row][2]))
    print("|       |       |       |")



def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    

    for i in range(3):
        print_divider()
        print_coordinates(board,i)

    print_divider()


# def enter_human_move(board):
#     move = int(input("Su turno. Ingrese un movimiento valido:"))
#     if move >= 0 and move <=9:
#         free_files = make_list_of_free_fields(board)
#         if (move in free_files):
#             push_move(move,board,0)
#     else:
#         print("Movimiento Invalido")
    
def push_move(movement,board,player):
    #Defino un diccionario con la equivalencias de los números con las coordenadas en el tablero. Por ejemplo si introduzco un uno se que las coordenadas son (0,0) y así
    equivalences = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    coordinates = equivalences[movement]
    if player == 0:
        board[coordinates[0]][coordinates[1]] = "X"
    if player == 1:
        board[coordinates[0]][coordinates[1]] = "O"        

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_coords = []
    for i in range(3):                                           #Barrido por columnas
        for j in range(3):                                       #Barrido por filas
            if board[i][j] != "O" and board[i][j] != "X":
                free_coords.append(board[i][j])
    return free_coords

def playHuman(board):
    flag = 1
    while flag:
        os.system("clear")
        display_board(board)
        move = int(input("Su turno. Ingrese un movimiento valido:"))
        if move > 0 and move <10:
            free_files = make_list_of_free_fields(board)
            if (move in free_files):
                push_move(move,board,0)
                flag = 0
        else:
            print("Movimiento Invalido. Reintentar")
    

def playComputer(board):
    flag = 1
    while flag:
        os.system("clear")
        display_board(board)
        move = randrange(9)  
        free_files = make_list_of_free_fields(board)
        if(move in free_files):
            push_move(move,board,1)
            flag = 0



def whoPlays():
    turn = 0
    if turn == 0:
        playHuman()
        turn = 1
    else:
        if turn == 1:
            playComputer()
            turn = 0

def isThereaWinner(board):                                    #Deberia ser una funcion que determine si algun jugador ha llegado a cumplir la condicion del juego, retornando
    diagonal1 = []
    diagonal2 = []                                             #que jugador lo ha conseguido. debería ser invocada luego de cada movimiento correcto
    aux = [0,0]                                               # aux = [Ganador?,Jugador Ganador] Si hay ganador el primer elemento es 1 y el segundo elemento indica el jugador ganador.
                                                              # 0 = humano 1 = computadora
    for i in range(3):                                        # barrido de filas 
        if board[i].count("X") == 3:
            aux[0] = 1
            aux[1] = 0
            return aux                                   
        if board[i].count("O") == 3:
            aux[0] = 1
            aux[1] = 1
            return aux
    
    transposed_board = list(map(list,zip(*board)))

    for i in range(3):
        if transposed_board[i].count("X") == 3:
            aux[0] = 1
            aux[1] = 0
            return aux
        if transposed_board[i].count("O") == 3:
            aux[0] = 1
            aux[1] = 1
            return aux

    for i in range(3):
        diagonal1.append(board[i][i])
    for i in range(3):
        diagonal2.append(board[i][-i-1])
    
    for i in range(3):
        if diagonal1.count("X") == 3:
            aux[0] = 1
            aux[1] = 0
            return aux
        if diagonal1.count("O") == 3:
            aux[0] = 1
            aux[1] = 1
            return aux
    
    for i in range(3):
        if diagonal2.count("X") == 3:
            aux[0] = 1
            aux[1] = 0
            return aux
        if diagonal2.count("O") == 3:
            aux[0] = 1
            aux[1] = 1
            return aux
    
 

    return aux




############################################################ Sección Principal ############################################################

print("TIC-TAC-TOE")
print("Seleccione su movimiento (1-9):")
flag = 1
turn = 0 
board = initializeBoard()
game_status = []

#game_status = isThereaWinner(board)
#print(game_status) 

while flag:
    game_status = isThereaWinner(board)
    if game_status[0]==1:
        if game_status[1] == 0:
            os.system("clear")
            display_board(board) 
            print("Humano Gana!")
            flag = 0
        if game_status[1] == 1:
            os.system("clear")
            display_board(board)
            print("Computadora Gana!")
            flag = 0
    else:
        if turn == 0:
            playHuman(board)
            os.system("clear")
            display_board(board)
            turn = 1
        else:
            playComputer(board)
            os.system("clear")
            display_board(board)
            turn = 0  



# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   5   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+

