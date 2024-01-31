import random

# Almacenamos los puntos de salud y defensa del jugador y del oponente en tuplas
PS_jugador = (100, 100)
PS_oponente = (100, 100)

# Almacenamos los ataques en un diccionario
ataque_jugador = {"placaje": (35, 10),
                    "malicioso": (0, 10),
                    "ascuas": (20, 0)}
ataque_oponente = {"pistola de agua": (40, 0),
                    "latigo": (0, 10),
                    "placaje": (35, 0)}

# Almacenamos los ataques en una lista para poder acceder a ellos fácilmente
ataques = [ataque_jugador, ataque_oponente]

# Iniciamos el bucle while para el combate
while PS_jugador[0] > 0 and PS_oponente[0] > 0:
    # El jugador elige un ataque
    ataque_jugador = input("ataque: ")
    # Comprobamos si el ataque es válido
    if ataque_jugador not in ataque_jugador:
        print("Que estas haciendo?! tus ataques son maliciosos, placaje, y ascuas!")
        continue
  
    PS_oponente = (PS_oponente[0] - ataque_jugador[1], PS_oponente[1] - ataque_jugador[0])
    # Si la defensa del oponente es menor o igual a 0, la igualamos a 1
    if PS_oponente[1] <= 0:
        PS_oponente = (PS_oponente[0], 1)
    # Turno del oponente
    # El turno del oponente se define con un random
    ataque_oponente = random.randrange(1, 3+1)
    # Comprobamos si el ataque del oponente es válido
    if ataque_oponente not in ataque_oponente:
        print("Que estas haciendo?! tus ataques son pistola de agua, latigo, y placaje!")
        continue
    # Restamos los puntos de salud y defensa del jugador según el ataque del oponente
    PS_jugador = (PS_jugador[0] - ataque_oponente[1], PS_jugador[1] - ataque_oponente[0])
    # Si la defensa del jugador es menor o igual a 0, la igualamos a 1
    if PS_jugador[1] <= 0:
        PS_jugador = (PS_jugador[0], 1)

# Si termina el ciclo, alguien a ganado
if PS_oponente[0] <= 0 and PS_jugador[0] <= 0:
    print("empate")
elif PS_oponente[0] <= 0: # ya sabemos que el jugador es >0
    print("Felicitaciones, has ganado")
else: # ya sabemos que el componente es > 0
    print("Lo siento, has perdido")