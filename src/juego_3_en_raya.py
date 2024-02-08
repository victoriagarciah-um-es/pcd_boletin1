import pytest 
n = 0
fichas= ['o','x'] 


def generar_tablero(n, movimientos_jugadores): 
    tablero=[] 
    for i in range(n): 
        fila=['_' for i in range(n)] 
        for j in range(n): 
            casilla_vacia = True 
            for k in range(len(movimientos_jugadores)): 
                movimientos_jugador= movimientos_jugadores[k] 
 
                if i in movimientos_jugador: 
                    if j in movimientos_jugador[i]: 
                        fila[j]=fichas[k] 
        tablero.append(fila) 
    return tablero 


def  test_generar_tablero():  
    mov_jugador_1 = {}   
    mov_jugador_2 = {}   
    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]   
    n=3  
    t= generar_tablero(n, movimientos_jugadores)  
    assert len(t)== n  
    for f in t:  
        assert len(f) == n
        
        
""" 
Método que comprueba que un movimiento de un jugador es válido 
    * x: fila donde el jugador quiere colocar la ficha. 
    * y: columna donde el jugador quiere colocar su ficha. 
    * movimientos_otro_jugador: listado con las celdas ocupadas por el otro 
jugador. 
""" 
def movimiento_valido(x, y, movimientos_otro_jugador): 
    if x > n or y > n: 
        return False 
    if x in movimientos_otro_jugador: 
        movimientos_en_columna= movimientos_otro_jugador[x] 
        if y in movimientos_en_columna: 
            return False 
    return True 

def test_movimiento_columna_fuera_tablero(): 
    movimientos_otro_jugador={} 
    x=  1 
    y=  n+1 
    assert False == movimiento_valido(x,y,movimientos_otro_jugador) 
 
def test_movimiento_fila_y_columna_fuera_tablero(): 
    movimientos_otro_jugador={} 
    x=  n+1 
    y=  n+1 
    assert False == movimiento_valido(x,y,movimientos_otro_jugador) 
 
def test_movimiento_incorrecto(): 
    movimientos_otro_jugador={2:[3]} 
    x=  2 
    y=  3 
    assert False == movimiento_valido(x,y,movimientos_otro_jugador)
    
