# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 01:03:35 2024

@author: richa
"""

def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta é uma maçã!"    
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta é uma banana!"
    else:
      return "Não foi possível classificar a fruta."
# TODO: Desenvolva a Função para prever a classe da fruta


# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)