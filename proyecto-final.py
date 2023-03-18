import os
import random


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


def enter_human_move(board):
    move = int(input("Su turno. Ingrese un movimiento valido:"))
    if move >= 0 and move <=9:
        free_files = make_list_of_free_fields(board)
        if (move in free_files):
            push_move(move,board)
    else:
        print("Movimiento Invalido")
    
def push_move(movement,board):
    #Defino un diccionario con la equivalencias de los números con las coordenadas en el tablero. Por ejemplo si introduzco un uno se que las coordenadas son (0,0) y así
    equivalences = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    coordinates = equivalences[movement]
    board[coordinates[0]][coordinates[1]] = "X"

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_coords = []
    for i in range(3):                                           #Barrido por columnas
        for j in range(3):                                       #Barrido por filas
            if board[i][j] != "O" and board[i][j] != "X":
                free_coords.append(board[i][j])
    return free_coords

def playHuman():
    move = int(input("Su turno. Ingrese un movimiento valido:"))
    if move >= 0 and move <=9:
        free_files = make_list_of_free_fields(board)
        if (move in free_files):
            push_move(move,board)
    else:
        print("Movimiento Invalido")
    

def playComputer():
    move = 

def whoPlays():
    turn = 0
    if turn == 0:
        playHuman()
        turn = 1
    else:
        if turn == 1:
            playComputer()
            turn = 0

def checkGame(board):
    pass


############################################################ Sección Principal ############################################################

print("TIC-TAC-TOE")
print("Seleccione su movimiento (1-9):")
turn = 0

board = initializeBoard()

os.system("cls")
display_board(board)


while 1:
    checkGame(board)
    whoPlays() 




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

