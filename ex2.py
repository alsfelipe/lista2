uniforme = 0
isotonico = 0
raquete = 0 
toalha = 0

entrada = input()
while entrada != "FIM":
    if entrada == "Uniforme":
        uniforme += 1
        print(f"Tava faltando camisa! Agora temos {uniforme} uniforme(s)")
    elif entrada == "Isotônico":
        isotonico += 1
        print(f"Bora garantir a hidratação! Agora temos {isotonico} isotônico(s)")
    elif entrada == "Raquete":
        raquete += 1
        print(f"Mais uma raquete saindo! Agora temos {raquete} raquete(s)")
    elif entrada == "Toalha":
        toalha += 1
        print(f"Mais uma toalha saindo! Agora temos {toalha} toalha(s)")
    elif entrada == "Sabotagem":
        material_sabotado = input()
        if material_sabotado == "Uniforme":
            
    entrada = input()
    