#!/usr/bin/env python
# coding: utf-8

# In[1]:


def jogador1():
    n = 21
    while n > 1 :
        jog = int(input("introduza o número de fósforos a retirar: "))
        if jog > 0 and jog <= 4 :
            comp = 5 - jog
            print ("número de fósforos retirados pelo computador: ", comp)
            n = n - 5
            print ("fósforos restantes: ", n)
        else :
            print ("valor introduzido inválido")
    print ("computador ganhou!")


# In[2]:


import random
def jogador2():
    i = 0
    n = 21
    while n > 1 :
        comp = random.randint(1,4)
        print ("número de fósforos retirados pelo computador: ", comp)
        jog = int(input("introduza o número de fósforos a retirar: "))
        if jog > 0 and jog <= 4 :
            if (jog + comp) % 5 == 0 :
                n = n - 5
                print ("fósforos restantes: ", n)
                i = i + 1
            else :
                n = n - (jog + comp)
                print ("fósforos restantes: ", n)
                comp = 5 - ((jog + comp) % 5)
                print ("número de fósforos retirados pelo computador: ", comp)
                n = n - comp
                while n > 1 :
                    jog = int(input("introduza o número de fósforos a retirar: "))
                    if jog > 0 and jog <= 4 :
                        comp = 5 - jog
                        print ("número de fósforos retirados pelo computador: ", comp)
                        n = n - 5
                        print ("fósforos restantes: ", n)
                    else :
                        print ("valor introduzido inválido")
        else :
            print ("valor introduzido inválido")
    if i == 4 :
        print ("você ganhou!")
    else :
        print ("computador ganhou!")


# In[3]:


def jogarfósforos():
    jogador = int(input("introduza '1' ou '2' para jogar em primeiro ou segundo lugar, respetivamente: "))
    if jogador == 1 :
        jogador1()
    elif jogador == 2 :
        jogador2()
    else :
        print ("valor introduzido inválido")

