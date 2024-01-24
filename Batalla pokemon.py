import random

PS_jugador = 100
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

ataque_jugador = ['placaje', 'ascuas', 'malicioso']
ataque_oponente = ['pistola de agua', 'latigo', 'placaje']


while PS_jugador > 0 and PS_oponente > 0:
    ataque_jugador = input("ataque: ")
    if ataque_jugador == "malicioso":
        defensa_oponente = defensa_oponente - 10
        if defensa_oponente <= 0:
            defensa_oponente = 1
    elif ataque_jugador == "placaje":
        PS_oponente -= 35 / (defensa_oponente/100)
    elif ataque_jugador == "ascuas":
        PS_oponente -= 20
        pass
    else:
        print("Que estas haciendo?! tus ataques son maliciosos, placaje, y ascuas!")
        continue
    
    #turno oponente
    #El turno del oponente se define con un random
    ataque_oponente = random.randrange(1, 3+1)
    if ataque_oponente == 1: #latigo
        defensa_jugador = defensa_jugador - 10
        if defensa_jugador <= 0:
            defensa_jugador = 1
    elif ataque_oponente == 2: #placaje 
        PS_jugador -= 35 * (100/defensa_jugador)
    elif ataque_jugador == 3: #Pistola de agua
        PS_jugador -= 40
    #randrange está garantazado a ser 1,2 ó 3

#Si termina el ciclo, alguien a ganado 
if PS_oponente <= 0 and PS_jugador <= 0:
    print("empate")
elif PS_oponente <= 0: #ya sabes que el jugador es >0
    print("Felicitaciones, has ganado")
else: #ya sabemos que el componente es > 0
    print("Lo siento, has perdido")

    


