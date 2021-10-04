# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:03:20 2021

@author: Karina
"""

def imprimir(texto, valor):
    print('El texto ingresado es: '+ texto + ' y el valor ingresado es: '+ str(valor))
    
    
    
texts = input('Ingrese su texto: ')
valor = int(input('Ingrese un valor: '))


imprimir(texts, valor)