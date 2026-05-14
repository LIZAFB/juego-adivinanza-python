jugador1 = input("Jugador 1, elige piedra, papel o tijeras: ")
jugador2 = input("Jugador 2, elige piedra, papel o tijeras: ")  

if jugador1 == jugador2:    
    print("Empate!")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
    print("Jugador 1 gana!")
else:    
    print("Jugador 2 gana!")

