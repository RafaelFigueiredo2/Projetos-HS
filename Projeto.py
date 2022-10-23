import random

class GerarSimbolo:
    def __init__(self, simb):
        self.simb = simb
        self.roll()
    def roll(self):
        simbolos = [1, 2, 3, 4, 5, 6, 7]
        self.rand = (random.choices(simbolos, weights=(50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156)))
  
creditos = int(input("Creditos a depositar:  "))
while True:
    simbolo1 = GerarSimbolo(1)
    simbolo2 = GerarSimbolo(1)
    simbolo3 = GerarSimbolo(1)
    simb1 = (simbolo1.rand)    
    simb2 = (simbolo2.rand)    
    simb3 = (simbolo3.rand)  

    
    aposta = int(input("Creditos a apostar:  "))
    
    if aposta > creditos:
        print("Não tens creditos suficientes")
        continue
    
    creditos_atuais = creditos - aposta
    
    print(simb1, simb2, simb3)
    if not simb1 == simb2 == simb3:
        print("Não ganhaste nada. \n Ficas com {} creditos".format(creditos_atuais))
        creditos = creditos_atuais
        if creditos <= 0:
            break
            
        resposta = input("Continuar a jogar?")
        if resposta == "s" or resposta == "sim" or resposta == "S" or resposta == "Sim":
            continue
            
        else:
            break

            
    else:
        simbolo =  simb1
        if simbolo == [1]:
            ganhos = aposta * 5
        if simbolo == [2]:
            ganhos = aposta * 10
        if simbolo == [3]:
            ganhos = aposta * 20
        if simbolo == [4]:
            ganhos = aposta * 70
        if simbolo == [5]:
            ganhos = aposta * 200
        if simbolo == [6]:
            ganhos = aposta * 1000
        if simbolo == [7]:
            ganhos = aposta * 100000

            
        creditos = creditos_atuais + ganhos
        
        print("Ganhaste {} e ficas com {} creditos disponiveis".format(ganhos,creditos))
        resposta = input("Continuar a jogar?")
        
        if resposta == "s" or resposta == "sim" or resposta == "S" or resposta == "Sim":
            continue
        
        else:
            break
    
        
