print("Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!")
sacador = input()
acao2 = ""
contador_sets = 1
sets_hugo = 0
sets_lin = 0
acabou = False
tiebreak = False
while contador_sets < 6 and acabou == False:
    print(f"Set {contador_sets}")
    ponto_hugo = 0
    ponto_lin = 0
    Fim_set = False
    if contador_sets > 1:
        if sacador == "hugo":
            sacador = "lin"
        else:
            sacador = "hugo"
    if sets_hugo == 2 and sets_lin == 2 and tiebreak == False:
        tiebreak = True
        print("Agora é hora da decisão! Vamos para o tie-break, quem errar, perde tudo! É emoção até o fim!")
    while Fim_set == False:
        entrada = input()
        acao = str()
        numero_acao = 0
        for letra in entrada:
            pontuou = False
            if letra != "-":
                    acao += letra
                    if acao == ("saque") or acao == ("defesa") or acao == ("ataque") or acao == ("controle") or acao == ("erro"):
                        
                        numero_acao += 1

                        if numero_acao % 2 == 1:
                            if sacador == "hugo":
                                vez = "hugo"
                                naovez = "lin"
                            elif sacador == "lin":
                                vez = "lin"
                                naovez = "hugo"
                        else:
                            if sacador == "hugo":
                                vez = "lin"
                                naovez = "hugo"
                            elif sacador == "lin":
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

                            elif acao1 == "erro":
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
                                        quem_pontuou = "hugo"
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


                        if tiebreak == False:

                            if pontuou == True:

                                print(f"Ponto para {quem_pontuou}!")
                                print(f"Placar do {contador_sets} set : {ponto_hugo} x {ponto_lin}")
                                
                                if ponto_hugo == 4 and ponto_lin == 4:
                                    print("O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!")
                                elif ponto_hugo == 5 and ponto_lin == 0:
                                    Fim_set = True
                                    sets_hugo += 1
                                    print("Fim de set! Domínio total: 5 a 0, sem chance para o adversário — hugo passeia na mesa")
                                elif ponto_lin == 5 and ponto_hugo == 0:
                                    Fim_set = True
                                    sets_lin += 1
                                    print("Fim de set! Domínio total: 5 a 0, sem chance para o adversário — lin passeia na mesa")
                                elif ponto_hugo == 5 and (ponto_hugo - ponto_lin) >= 2:
                                    Fim_set = True
                                    sets_hugo += 1
                                    print("E o set vai para hugo!")
                                elif ponto_lin == 5 and (ponto_lin - ponto_hugo) >= 2:
                                    Fim_set = True
                                    sets_lin += 1
                                    print("E o set vai para lin!")
                                elif ponto_hugo > 5 and (ponto_hugo - ponto_lin) == 2:
                                    Fim_set = True
                                    sets_hugo += 1
                                    print("E o set vai para hugo!")
                                elif ponto_lin > 5 and (ponto_lin - ponto_hugo) == 2:
                                    Fim_set = True
                                    sets_lin += 1
                                    print("E o set vai para lin!")
                            
                            if Fim_set == True:
                                print(f"Placar do jogo: {sets_hugo} x {sets_lin}")
                                contador_sets += 1
                        
                
                        elif tiebreak == True:

                            if pontuou == True:

                                print(f"Ponto para {quem_pontuou}!")
                                print(f"Placar do {contador_sets} set : {ponto_hugo} x {ponto_lin}")   

                                if ponto_hugo == 7 and ponto_lin == 0:
                                    Fim_set = True
                                    sets_hugo += 1
                                    print("Fim de tie-break! hugo arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!")        
                                elif ponto_hugo == 0 and ponto_lin == 7:
                                    Fim_set = True          
                                    sets_lin += 1
                                    print("Fim de tie-break! lin arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!")
                                if ponto_hugo == 6 and ponto_lin == 6:
                                    print("O tie-break está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva, é a reta final da disputa! Quem será o grande campeão?")
                                elif (ponto_hugo - ponto_lin) == 2 and ponto_hugo >= 8:
                                    Fim_set = True
                                    sets_hugo += 1
                                    print("E o set vai para hugo!")
                                elif (ponto_lin - ponto_hugo) == 2 and ponto_lin >= 8:
                                    Fim_set = True
                                    sets_lin += 1
                                    print("E o set vai para lin!")
                                elif ponto_hugo == 7 and (ponto_hugo - ponto_lin) >= 2:
                                    Fim_set = True
                                    sets_hugo += 1
                                    print("E o set vai para hugo!")
                                elif ponto_lin == 7 and (ponto_lin - ponto_hugo) >= 2:
                                    Fim_set = True
                                    sets_hugo += 1
                                    print("E o set vai para lin!")
                                
                            if Fim_set == True:
                                print(f"Placar do jogo: {sets_hugo} x {sets_lin}")
                                contador_sets += 1
                                

                        if sets_hugo == 3:
                            acabou = True
                            vencedor = "hugo"
                        elif sets_lin == 3:
                            acabou = True
                            vencedor = "lin"
                        
                        acao = ""
        acao1 = ""
        acao2 = ""

if acabou == True:
    if vencedor == "hugo":
        if tiebreak == False:
            print("Hugo garantiu a vitória sem precisar de tie-break! Uma performance sólida e sem erros, ele dominou o jogo do início ao fim e se sagrou campeão do mundo!")
        elif tiebreak == True:
            print("Hugo é o grande vencedor! Ele conquista o tie-break com uma performance impecável e leva a vitória!")
    elif vencedor == "lin":
        if tiebreak == False:
            print("Hugo não conseguiu segurar a pressão e acabou perdendo sem precisar do tie-break. Foi uma grande final, mas hoje não foi o seu dia. Vitória do chinês!")
        elif tiebreak == True:
            print("Hugo lutou até o fim, mas no tie-break, o adversário levou a melhor. Uma derrota apertada, mas ainda assim, uma grande batalha!")
