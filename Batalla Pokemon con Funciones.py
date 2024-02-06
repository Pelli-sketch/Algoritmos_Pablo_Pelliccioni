import random

def malicioso(PS_jugador):
    PS_jugador = (PS_jugador[0], PS_jugador[1] - 10)
    if PS_jugador[1] <= 0:
        PS_jugador = (1, PS_jugador[1])
    return PS_jugador

def placaje(PS_jugador):
    PS_jugador = (
        PS_jugador[0] - 35 / (PS_jugador[1]/100),
        PS_jugador[1],
    )
    return PS_jugador

def ascuas(PS_jugador):
    PS_jugador = (PS_jugador[0] - 20, PS_jugador[1])
    return PS_jugador

def latigo(PS_jugador):
    PS_jugador = (PS_jugador[0], PS_jugador[1] - 10)
    if PS_jugador[1] <= 0:
        PS_jugador = (PS_jugador[0], 1)
    return PS_jugador

def pistola_agua(PS_jugador):
    PS_jugador = (PS_jugador[0] - 40, PS_jugador[1])
    return PS_jugador

PS_jugador = (100, 100)
PS_oponente = (100, 100)

while PS_jugador[0] > 0 and PS_oponente[0] > 0: 
    ataque_jugador = input("ataque: ")
    if ataque_jugador == "malicioso":
        PS_oponente = malicioso(PS_oponente)
    elif ataque_jugador == "placaje":
        PS_oponente = placaje(PS_oponente)
    elif ataque_jugador == "ascuas":
        PS_oponente = ascuas(PS_oponente)
    else:
        print("Que estas haciendo?! tus ataques son malicioso, placaje, y ascuas!")
        continue

    # turno oponente
    ataque_oponente = random.randrange(1, 3+1)
    if ataque_oponente == 1:  # latigo
        PS_jugador = latigo(PS_jugador)
    elif ataque_oponente == 2:  # placaje
        PS_jugador = placaje(PS_jugador)
    elif ataque_oponente == 3:  # Pistola de agua
        PS_jugador = pistola_agua(PS_jugador)

# Si termina el ciclo, alguien a ganado
if PS_oponente[0] <= 0 and PS_jugador[0] <= 0:
    print("empate")
elif PS_oponente[0] <= 0:  # ya sabes que el jugador es >0
    print("Felicitaciones, has ganado")
else:  # ya sabemos que el componente es > 0
    print("Lo siento, has perdido")