
import random

class Agora:
    def __init__(self, simb):
        self.simb = simb
        self.roll()
    def roll(self):
        simbolos = [1, 2, 3, 4, 5, 6, 7]
        self.rand = (random.choices(simbolos, weights=(50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156)))
  

x0 = 1
creditos = int(input("Creditos a depositar:  "))
while x0 == 1:
    simbolo1 = Agora(1)
    simbolo2 = Agora(1)
    simbolo3 = Agora(1)
    simb1 = (simbolo1.rand)    
    simb2 = (simbolo2.rand)    
    simb3 = (simbolo3.rand)  

    creditos_atuais = creditos
    aposta = int(input("Creditos a apostar:  "))
    creditos_atuais = creditos_atuais - aposta
    
    print(simb1, simb2, simb3)




    if not simb1 == simb2 == simb3:
        print("Não ganhaste nada. \n Ficas com {} creditos".format(creditos_atuais))
        creditos = creditos_atuais
        if creditos <= 0:
            break
        resposta = input("Continuar a jogar?")
        if resposta == "s" or resposta == "sim" or resposta == "S" or resposta == "Sim":
            x0 = 1
        else:
            x0 = 0




    else:
        d =  simb1
        y = aposta
        if d == [1]:
            w = y * 5
        if d == [2]:
            w = y * 10
        if d == [3]:
            w = y * 20
        if d == [4]:
            w = y * 70
        if d == [5]:
            w = y * 200
        if d == [6]:
            w = y * 1000
        if d == [7]:
            w = y * 100000

        creditos = creditos_atuais + w
        print("Ganhaste {} e ficas com {} creditos disponiveis".format(y,creditos))
        resposta = input("Continuar a jogar?")
        if resposta == "s" or resposta == "sim" or resposta == "S" or resposta == "Sim":
            x0 =1
        else:
            x0 = 0
    
        
