ataque = 0
defesa = 0
errou = 0
print("------- Início do Treino -------")
n =  int(input())
for i in range(0, n):
    bola_lancada = str(input())
    golpe_executado = str(input())
    #Ataque
    if bola_lancada == "Ataque":
        if golpe_executado == "Smash":
            print(f"Você conseguiu rebater uma bola de {bola_lancada}! Golpe executado: {golpe_executado}.")
            ataque += 10
        elif golpe_executado == "Topspin":
            print(f"Você conseguiu rebater uma bola de {bola_lancada}! Golpe executado: {golpe_executado}.")
            ataque += 5
        elif golpe_executado == "Errou":
            print("Você errou! Levanta a cabeça que ainda tem mais.")
            ataque -= 10
            errou = 10
    #Defesa
    elif bola_lancada == "Defesa":
        if golpe_executado == "Chop":
            print(f"Você conseguiu rebater uma bola de {bola_lancada}! Golpe executado: {golpe_executado}.")
            defesa += 10
        elif golpe_executado == "Push":
            print(f"Você conseguiu rebater uma bola de {bola_lancada}! Golpe executado: {golpe_executado}.")
            defesa += 5
        elif golpe_executado == "Errou":
            print("Você errou! Levanta a cabeça que ainda tem mais.")
            defesa -= 10
            errou = 10
if ataque < 0: 
    ataque = 0
if defesa < 0:
    defesa = 0            
if ataque > defesa:
    print("Ter um bom jogo ofensivo será fundamental para ganhar o InterCin!")
elif defesa > ataque:
    print("Defesa ganha campeonatos! Agora sim estou preparado.")
else:
    print("Foi um treino equilibrado.")
if errou == 10:
    print("Infelizmente não foi um treino perfeito, mas pude melhorar muito.")
print("------- Atributos -------")
print(f"Ataque: {ataque}")
print(f"Defesa: {defesa}")