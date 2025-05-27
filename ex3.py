classica = 0
caneta = 0
classineta = 0
pessoas = int(input())
for i in range(0, pessoas):
    voto = input()
    if voto == "Clássica":
        classica += 1
    elif voto == "Caneta":
        caneta += 1
    elif voto == "Classineta":
        classineta += 1
print("Estamos calculando... tão rápido quanto dar Run no Dikastis...")
#Classica primeiro
if classica > caneta and classica > classineta:
    primeiro = classica
    nome1 = "Clássica"
    if caneta > classineta:
        segundo = caneta
        nome2 = "Caneta"
        terceiro = classineta
        nome3 = "Classineta"
    else:
        segundo = classineta
        nome2 = "Classineta"
        terceiro = caneta
        nome3 = "Caneta"
#Caneta Primeiro
elif caneta > classica and caneta > classineta:
    primeiro = caneta
    nome1 = "Caneta"
    if classica > classineta:
        segundo = classica
        nome2 = "Clássica"
        terceiro = classineta
        nome3 = "Classineta"
    else:
        segundo = classineta
        nome2 = "Classineta"
        terceiro = classica
        nome3 = "Clássica"
#Classineta Primeiro
elif classineta > classica and classineta > caneta:
    primeiro = classineta
    nome1 = "Classineta"
    if classica > caneta:
        segundo = classica
        nome2 = "Clássica"
        terceiro = caneta
        nome3 = "Caneta"
    else:
        segundo = caneta
        nome2 = "Caneta"
        terceiro = classica
        nome3 = "Clássica"
print(f"1º lugar: {nome1} ({primeiro} votos)")
print(f"2º lugar: {nome2} ({segundo} votos)")
print(f"3º lugar: {nome3} ({terceiro} votos)")
if primeiro == classica and primeiro - segundo >= 5:
    print("Podemos ver que a influência do grande Hugo Calderano foi disseminada pelos corredores do CIn!")
    