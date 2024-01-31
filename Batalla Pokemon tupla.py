import random

PS_jugador = (100, 100)  # (vida, defensa)
PS_oponente = (100, 100)

ataque_jugador = { #Actualice los diccionarios para que almacenen tuplas
    "placaje": (35, 10),
    "malicioso": (0, 10),
    "ascuas": (20, 0),
}

ataque_oponente = {
    "pistola de agua": (40, 0),
    "latigo": (10, 10),
    "placaje": (35, 0),
}

#en el caso del jugador, usé PS_jugador[0] para acceder a los puntos de salud y PS_jugador[1] para acceder a los puntos de defensa.
#al igual con el oponente
#PS_oponente/jugador[0] --> VIDA
#PS_oponente/jugador[1] --> DEFENSA


while PS_jugador[0] > 0 and PS_oponente[0] > 0: 
    ataque_jugador = input("ataque: ")
    if ataque_jugador == "malicioso":
        PS_oponente = (PS_oponente[0], PS_oponente[1] - 10)
        if PS_oponente[1] <= 0:
            PS_oponente = (1, PS_oponente[1])
    elif ataque_jugador == "placaje":
        PS_oponente = (
            PS_oponente[0] - 35 / (PS_oponente[1]/100),
            PS_oponente[1],
        )
    elif ataque_jugador == "ascuas":
        PS_oponente = (PS_oponente[0] - 20, PS_oponente[1])
    else:
        print("Que estas haciendo?! tus ataques son malicioso, placaje, y ascuas!")
        continue

    # turno oponente
    ataque_oponente = random.randrange(1, 3+1)
    if ataque_oponente == 1:  # latigo
        PS_jugador = (PS_jugador[0], PS_jugador[1] - 10)
        if PS_jugador[1] <= 0:
            PS_jugador = (PS_jugador[0], 1)
    elif ataque_oponente == 2:  # placaje
        PS_jugador = (
            PS_jugador[0] - 35 / (PS_jugador[1]/100),
            PS_jugador[1],
        )
    elif ataque_oponente == 3:  # Pistola de agua
        PS_jugador = (PS_jugador[0] - 40, PS_jugador[1])

# Si termina el ciclo, alguien a ganado
if PS_oponente[0] <= 0 and PS_jugador[0] <= 0:
    print("empate")
elif PS_oponente[0] <= 0:  # ya sabes que el jugador es >0
    print("Felicitaciones, has ganado")
else:  # ya sabemos que el componente es > 0
    print("Lo siento, has perdido")