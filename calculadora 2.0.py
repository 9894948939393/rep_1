import math
import time
print("Os sinas são + adicção - subtração x multiplicação / divisão // raiz quadrada xx potenciação e = para obter o resultado")
time.sleep(3)
while True:
    numero = float(input("Digite o primeiro valor"))
    sinal = input("Digite o sinal")
    if sinal == "+":
        segundo_numero = float(input("Digite o proximo número"))
        total = numero + segundo_numero
        operação = f"{numero} " + sinal + f" {segundo_numero}"
    elif sinal == "-":
        segundo_numero = float(input("Digite o proximo número"))
        total = numero - segundo_numero
        operação = f"{numero} " + sinal + f" {segundo_numero}"
    elif sinal == "x":
        segundo_numero = float(input("Digite o proximo número"))
        total = numero * segundo_numero
        operação = f"{numero} " + sinal + f" {segundo_numero}"
    elif sinal == "/":
        segundo_numero = float(input("Digite o proximo número"))
        total = numero / segundo_numero
        operação = f"{numero} " + sinal + f" {segundo_numero}"
    elif sinal == "xx":
        segundo_numero = float(input("Digite o proximo número"))
        total = numero ** segundo_numero
        operação = f"{numero} " + sinal + f" {segundo_numero}"
    elif sinal == "//":
        operação = f"{sinal} {numero}"
        total = math.sqrt(numero)
    else:
        print("Ops, ocorreu um erro, tente novamente")
        break
    while True:
        sinal = input("Digite o sinal")
        if sinal != "=":
          if sinal == "+":
            proximo_numero = float(input("Digite o proximo número"))
            total += proximo_numero
            operação += " " + sinal + f" {proximo_numero}" 
          elif sinal == "-":
            proximo_numero = float(input("Digite o proximo número"))
            total -= proximo_numero
            operação += " " + sinal + f" {proximo_numero}"
          elif sinal == "x":
              proximo_numero = float(input("Digite o proximo número"))
              total *= proximo_numero
              operação += " " + sinal + f" {proximo_numero}"  
          elif sinal == "/":
              proximo_numero = float(input("Digite o proximo número"))
              total /= proximo_numero
              operação += " " + sinal + f" {proximo_numero}"  
          elif sinal == "//":
              print("caso vc queira fazer a raiz de toda a operação digite um caso queira fazer de um número esepcífico digite 2")
              time.sleep(2)
              radiciação = int(input("Qual o tipo?"))
              if radiciação == 1:
                proximo_numero = total
                operação += " " + sinal  
                total = math.sqrt(proximo_numero)
              elif radiciação == 2:
                proximo_numero = float(input("Digite o proximo número"))
                print("Qual sinal irá proceder a radiciação")
                time.sleep(1)
                sinal_radiciação = input("Digite o sinal")
                if sinal_radiciação == "+":
                  total += math.sqrt(proximo_numero)
                  operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}" 
                  print("Finalização da raiz, prossiga com a equação")
                elif sinal_radiciação == "-":
                  total -= math.sqrt(proximo_numero)
                  operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}" 
                  print("Finalização da raiz, prossiga com a equação")
                elif sinal_radiciação == "*":
                  total *= math.sqrt(proximo_numero)
                  operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}"
                  print("Finalização da raiz, prossiga com a equação") 
                elif sinal_radiciação == "/":
                  total /= math.sqrt(proximo_numero)
                  operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}" 
                  print("Finalização da raiz, prossiga com a equação")
                elif sinal_radiciação == "**":
                  total **= math.sqrt(proximo_numero)
                  operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}" 
                  print("Finalização da raiz, prossiga com a equação")
                elif sinal_radiciação == "//":
                  numero_radiciação = proximo_numero
                  funcionar = True
                  while funcionar == True:
                    sinal_radiciação = ""
                    numero_radiciação = numero_radiciação
                    print("Qual sinal irá proceder a radiciação")
                    time.sleep(1)
                    sinal_radiciação = input("Digite o sinal")
                    if sinal == "+":
                        proximo_numero = float(input("Digite o proximo número"))
                        total += math.sqrt(proximo_numero)
                        operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}" 
                        funcionar = False
                    elif sinal == "-":
                        proximo_numero = float(input("Digite o proximo número"))
                        total -= math.sqrt(proximo_numero)
                        operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}" 
                        funcionar = False
                    elif sinal == "*":
                        proximo_numero = float(input("Digite o proximo número"))
                        total *= math.sqrt(proximo_numero)
                        operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}" 
                        funcionar = False
                    elif sinal == "/":
                        proximo_numero = float(input("Digite o proximo número"))
                        total /= math.sqrt(proximo_numero)
                        operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}" 
                        funcionar = False
                    elif sinal == "**":
                        proximo_numero = float(input("Digite o proximo número"))
                        total **= math.sqrt(proximo_numero)
                        operação += " " + sinal_radiciação + " "+ sinal + f" {proximo_numero}"
                        funcionar = False
                    elif sinal == "//":
                        proximo_numero = float(input("Digite o proximo número"))
                        vazio = 0
                    else:
                        print("ops, sua operação não pode ser realizada, tente novamente")   
              else:
                print("Esta operação não pode ser realizada,tente novamente")
                break
          elif sinal == "xx":
              proximo_numero = float(input("Digite o proximo número"))
              total **= proximo_numero
              operação += " " + sinal + f" {proximo_numero}"  
        elif sinal == "=":
            print(f"Sua equação ficou {operação} = {total}")
            break
        else:
            print("Ops, ocorreu um erro tente novamente")
            break
         
