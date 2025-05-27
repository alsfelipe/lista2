
print("Robô Hugo 4.0 foi inicializado…")
F_Max = int(input())
forca_inicial = int(input())
nivel = input()
forca_media_jogador = int(input())

if nivel == "facil":
    print("Iniciando no modo iniciante... Ótimo para aquecer os motores!")
    incremento = 1
elif nivel == "medio":
    print("Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!")
    incremento = 3
else:
    print("Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!")
    incremento = 5

tempo = 0
forca_acumulada = 0
rebatida = 0
jogo = True
while jogo:
    tempo += 1
    rebatida = forca_inicial + (tempo * incremento)
    if rebatida <= 150:
        forca_acumulada += rebatida
        print(f"Rebatida {tempo}: força = {rebatida}, força acumulada = {forca_acumulada}")
    
    if rebatida > 150:
        print("Bola fora! A força da rebatida excedeu os limites da mesa.")
        jogo = False
    
    if forca_acumulada > F_Max:
        print("Energia do robô esgotada! Encerrando o confronto…")
        jogo = False

forca_media_robo = forca_acumulada // tempo

#Finalização
print("Partida finalizada! Estas são as estatísticas do embate:")
print(f"O robô realizou {tempo} rebatidas em {tempo} segundos, com força total de {forca_acumulada}.")
print(f"Força média do robô: {forca_media_robo}")
print(f"Força média do jogador: {forca_media_jogador}")
if forca_media_robo > forca_media_jogador:
    print("Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!")
elif forca_media_jogador > forca_media_robo:
    print("Vitória do jogador! O talento humano ainda é imbatível!")
else:
    print("Empate técnico! Um duelo digno de mestres do tênis de mesa.")
