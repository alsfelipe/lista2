print("Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!")
sacador = input()
if sacador == "hugo":
      oponente = "lin"
elif sacador == "lin":
      oponente = "hugo"
contador_sets = 1
ponto_hugo = 0
ponto_lin = 0
acabou = False
tiebreak = False
while contador_sets < 5 and acabou == False:
    print(f"Set {contador_sets}")
    entrada = input()
    acao = str()
    for letra in entrada:
           pontuou = False
           numero_acao = 0
           if letra != "-":
                acao += letra
                if acao == ("saque") or acao == ("defesa") or acao == ("ataque") or acao == ("coltrole") or acao == ("erro"):
                    
                    numero_acao += 1

                    if numero_acao % 2 == 1:
                        if sacador == "hugo":
                            vez = "hugo"
                            naovez = "lin"
                        if sacador == "lin":
                            vez = "lin"
                            naovez = "hugo"
                    else:
                        if sacador == "hugo":
                            vez = "lin"
                            naovez = "hugo"
                        if sacador == "lin":
                            vez = "hugo"
                            naovez = "lin"
                         
                    acao_momento = acao

                    if numero_acao % 2 == 1:
                        acao1 = acao_momento 

                        if acao2 == "ataque":
                             if acao1 != "defesa":
                                pontuou = True
                                if vez == "hugo":
                                    ponto_lin += 1
                                    quem_pontuou = "lin"
                                else:
                                    ponto_hugo += 1
                                    quem_pontuou = "hugo"
                                print(f"{naovez} acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")

                        elif acao2 == "defesa":
                            if acao1 == "defesa":
                                pontuou = True
                                if vez == "hugo":
                                    ponto_lin += 1
                                    quem_pontuou = "lin"
                                else:
                                    ponto_hugo += 1
                                    quem_pontuou = "hugo"
                                print(f"{vez} tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.")

                        if acao1 == "erro":
                            pontuou = True
                            if vez == "hugo":
                                ponto_lin += 1
                                quem_pontuou = "lin"
                            else:
                                ponto_hugo += 1
                                quem_pontuou = "hugo"
                            print(f"{vez} se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                                    
                    if numero_acao % 2 == 0:
                        acao2 = acao_momento

                        if acao1 ==  "saque":
                            if acao2 == "ataque" or acao2 == "erro":
                                pontuou = True
                                if vez == "hugo":
                                    ponto_lin += 1
                                    quem_pontuou = "lin"
                                else:
                                    ponto_hugo += 1
                                    quem_pontuou = 'hugo'
                                print(f"Uau, um ace! {naovez} solta o braço e deixa o adversário parado!")
                        
                        elif acao1 == "ataque":
                            if acao2 != "defesa":
                                pontuou = True
                                if vez == "hugo":
                                    ponto_lin += 1
                                    quem_pontuou = "lin"
                                else:
                                    ponto_hugo += 1
                                    quem_pontuou = "hugo"
                                print(f"{naovez} acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                            
                        elif acao1 == "defesa":
                            if acao2 == "defesa":
                                pontuou = True
                                if vez == "hugo":
                                    ponto_lin += 1 
                                    quem_pontuou = "lin"
                                else:
                                    ponto_hugo += 1
                                    quem_pontuou = "hugo"
                                print(f"{vez} tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.")

                        elif acao2 == "erro":
                            pontuou = True
                            if vez == "hugo":
                                ponto_lin += 1
                                quem_pontuou = "lin"
                            else:
                                ponto_hugo += 1
                                quem_pontuou = "hugo"
                            print(f"{vez} se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    
                    if pontuou == True:
                        print(f"Ponto para {quem_pontuou}!")
                        print(f"Placar do {contador_sets} set : {ponto_hugo} x {ponto_lin}")

                        if ponto_hugo == 4 and ponto_lin == 4 and tiebreak == False:
                            print("O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!")
                                                            