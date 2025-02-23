quantidade = int(input("Quantas notas são?"))
nota = [0]
tipo_de_notas = []
soma = 0
for i in range(0,quantidade,1):
    nota.insert(1, int(input("Indique o valor da nota")))
    soma += nota[1]
    if nota[1] == 2 and 2 not in tipo_de_notas:
        tipo_de_notas.insert(1, 2)
    elif nota[1] == 5 and 5 not in tipo_de_notas:
        tipo_de_notas.insert(1, 5)
    elif nota[1] == 10 and 10 not in tipo_de_notas:
        tipo_de_notas.insert(1, 10)
    elif nota[1] == 20 and 20  not in tipo_de_notas:
        tipo_de_notas.insert(1, 20)
    elif nota[1] == 50 and 50 not in tipo_de_notas:
        tipo_de_notas.insert(1, 50)
    elif nota[1] == 100 and 100 not in tipo_de_notas:
        tipo_de_notas.insert(1, 100)
    elif nota[1] == 200 and 200 not in tipo_de_notas:
        tipo_de_notas.insert(1, 200)
print(f" As suas notas foram {tipo_de_notas}" \
       f"O seu sotal de dinheiro foi {soma}, com uma quantidade de notas {len(nota)-1} e uma média de {soma/quantidade} reais por nota")