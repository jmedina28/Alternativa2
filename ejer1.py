"""El trabajo que realizaremos consiste en la elaboración de un modelo para resolver sudokus, para ello, crea una función que resuelva un Sudoku de 9x9.
Un sudoku es un tablero matemático que se construye sobre una rejilla de 9x9 casillas. El objetivo es rellenarla con números enteros del 1 al 9 según las siguientes restricciones: 
·  No se pueden repetir números en una misma fila.
·  No se pueden repetir números en una misma columna.
·  No se pueden repetir números en una misma subcuadrícula de 3x3 de las 9 que componen la rejilla.
·  Esta función recibe un argumento que consiste en una matriz de 2D. Un valor de 0 representa un cuadrado desconocido.
El sudoku a resolver ha de estar bien planteado, i.e., ha de tener solución única. Esto se cumple si se parte de unas condiciones iniciales adecuadas, que consisten en números ya fijados en algunas de las casillas del sudoku"""

tablero = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def valido(tablero, intento, i, j):
    fila_valida = intento not in tablero[i]
    columna_valida = intento not in (tablero[k][j] for k in range(9))
    subcuadricula_valida = intento not in (tablero[i - i % 3 + m][j - j % 3 + n] 
                                  for n in range(3) 
                                  for m in range(3))
    return fila_valida and columna_valida and subcuadricula_valida