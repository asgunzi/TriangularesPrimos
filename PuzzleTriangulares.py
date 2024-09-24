#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:49:25 2024

@author: asgunzi
"""

import math

def isPrime(N):
    #Rotina simples para identificar um número primo

    if N ==2:
        return(True)
    elif N % 2 ==0:
        return(False)
    else:
        nMax = math.ceil(math.sqrt(N))
        status = True
        for i in range(3, nMax+1, 2):
            if N % i == 0:  
                status = False
                break
        
        return(status)
            
    


def numTriangular(N):
    #Gera números triangulares    
    t =0
    tval = 0
    lstTriang =[]
    continuar = True
    
    while continuar:
        
        t+=1
        
        tval = sum(list(range(1,t+1)))
        
        
        if tval  < N:
            lstTriang.append(tval) 
        else:
            continuar = False
    
    return(lstTriang)


lstTriang = numTriangular(2000000)

#Verifica quem é primo
lstPrimos =[]
for t in lstTriang:
    if isPrime(t):
        lstPrimos.append(t)

print(lstPrimos)


        