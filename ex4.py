tempo = 1

print("Robô Hugo 4.0 foi inicializado…")

F_Max = int(input())
forca_inicial = int(input())
nivel = input()
forca_media_jogador = int(input())
#Definindo a dificuldade
if nivel == "facil":
    print("Iniciando no modo iniciante... Ótimo para aquecer os motores!")
    incremento = 1
elif nivel == "medio":
    print("Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!")
    incremento = 3
else:
    print("Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!")
    incremento = 5
#Rebatida e Força Acumulada
rebatida = forca_inicial + (tempo * incremento)
forca_acumulada = rebatida
#Laço
print(f"Rebatida {tempo}: força = {rebatida}, força acumulada = {forca_acumulada}")
while forca_acumulada < F_Max and rebatida <= 150:
    tempo += 1
    rebatida = forca_inicial + (tempo * incremento)
    forca_acumulada += rebatida
    print(f"Rebatida {tempo}: força = {rebatida}, força acumulada = {forca_acumulada}")
#Condicionais
if forca_acumulada > F_Max:
    print("Energia do robô esgotada! Encerrando o confronto…")
elif rebatida > 150:
    print("Bola fora! A força da rebatida excedeu os limites da mesa.")
#Cáuculos Finais
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
    