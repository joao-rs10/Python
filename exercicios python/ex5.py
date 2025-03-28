

votosbrancos= int(input("Números de votos brancos: "))
votosnulos= int(input("Números de votos nulos: "))
votosvalidos= int(input("Números de votos válidos: "))

total= votosbrancos + votosnulos + votosvalidos

brancos= votosbrancos/total *100
nulos= votosnulos/total *100
validos= votosvalidos/total *100

print(f"Os votos brancos representasm {brancos}%, os votos nulos representam {nulos}%, os votos validos representam {validos}%, do total de {total} votos")