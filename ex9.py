rebatidas = 0
ponto1 = 0
ponto2 = 0
contador_sets = 1
contador_rebatidas = 0
acabou = False
sets_jogador1 = 0
sets_jogador2 = 0
acabou_set = False

jogador1 = input()
jogador2 = input()

if (jogador1 == "Luis" or jogador1 == "Lavoisier" or jogador1 == "Joab" or jogador1 == "Renan") and (jogador2 == "Luis" or jogador2 == "Lavoisier" or jogador2 == "Joab" or jogador2 == "Renan"):
    print("Essa partida vai ser épica! O jogo vai ser emocionante!")

num_sets = int(input())

nivel_disputa = input()

if nivel_disputa == "aprendizes":
    rebatidas = 1
elif nivel_disputa == "básicos":
    rebatidas = 2
else:
    rebatidas = 3

while contador_sets <= num_sets:
    sacador = jogador1
    print(f"Iniciando o {contador_sets}º set")
    
    acabou_set = False
    while acabou_set == False:
        acabou = False
        print(f"O saque é de {sacador}")
        acao = input()
        #Saque
        if acao ==  "saque":
            entrada1 = input()
            entrada2 = input()
            #Acertou o saque
            if entrada1 ==  "SA" and entrada2 == "AO":
                print(("Um saque PERFEITO!!"))
                acao = input()
            else:
                if entrada1 == "SA" and entrada2 == "SA":                
                    if sacador == jogador1:
                        oponente = jogador2
                        ponto2 += 1
                    else:
                        oponente = jogador1
                        ponto1 += 1
                    print(f"{sacador}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??")   
                    sacador = oponente

                elif entrada1 == "AO" and entrada2 == "AO":
                    if sacador == jogador1:
                        oponente = jogador2
                        ponto2 += 1
                    else:
                        oponente = jogador1
                        ponto1 += 1
                    print(f"Boa, {sacador}! Deu ponto de graça pro oponente!! Agora quem saca é {oponente}")
                    sacador = oponente

                elif entrada1 == "REDE" or entrada2 == "REDE":
                    if sacador == jogador1:
                        oponente = jogador2
                        ponto2 += 1
                    else:
                        oponente = jogador1
                        ponto1 += 1
                    print("Vish, ainda bateu na rede")
        #Rebatida
        if acao == "rebatida":
                while contador_rebatidas < rebatidas and acabou == False:
                    entrada_acao = input()
                    if entrada_acao == f"{jogador1} deixou a bola cair":
                        ponto2 += 1
                        sacador = jogador2
                        acabou = True
                        contador_rebatidas = 0
                    elif entrada_acao == f"{jogador2} deixou a bola cair":
                        ponto1 += 1
                        sacador = jogador1
                        acabou = True
                        contador_rebatidas = 0
                    elif entrada_acao == "oponente rebateu":
                        contador_rebatidas += 1
                if acabou == False:
                    contador_rebatidas = 0
                    velocidade_jogador1 = int(input())
                    velocidade_jogador2 = int(input())
                    if velocidade_jogador1 < velocidade_jogador2:
                        ponto1 += 1
                        sacador = jogador1
                    elif velocidade_jogador2 < velocidade_jogador1:
                        ponto2 += 1
                        sacador = jogador2
                                
        
        if (ponto1 - ponto2) >= 2 and ponto1 >= 3:
            sets_jogador1 += 1
            contador_sets += 1
            ponto1 = 0
            ponto2 = 0
            acabou_set = True
        elif (ponto2 - ponto1) >= 2 and ponto2 >= 3:
            sets_jogador2 += 1
            contador_sets += 1
            ponto1 = 0
            ponto2 = 0
            acabou_set = True
#Definindo Vencedor
if sets_jogador1 > sets_jogador2:
    vencedor = jogador1
else:
    vencedor = jogador2

print(f"Depois de {num_sets} set(s) vibrante(s), o grande vencedor é {vencedor}!!")
print("Fim do jogo!")