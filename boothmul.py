# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:41:57 2024

@author: Lenovo
"""
def addb(l1, l2):

    l3=[0 for x in range(len(l2))]
    cry=0
    i=len(l3)-1
    while(i>=0):
        r = l1[i] + l2[i] + cry
        if r==3:
            l3[i] = 1
            cry   = 1
        elif r==2:
            l3[i] = 0
            cry   = 1
        elif r==1:
            l3[i] = 1
            cry   = 0
        elif r==0:
            l3[i] = 0
            cry   = 0
        i=i-1
    return l3

def twos_comp(l):
    L = l[:]
    for i in range(len(L)):
        if L[i] == 0:
            L[i] = 1
        elif L[i] == 1:
            L[i] = 0
    second_operand = [0 for x in range(len(L))]
    second_operand[len(L)-1] = 1
    return addb(L,second_operand) #returns a list

def arshift(L):
    l = [0 for x in range(len(L))]
    for i in range(len(L)-1):
            l[i+1] = L[i]

    if(L[0] == 1):
        l[0] = 1
    
    return l

def binary(M):

    rem=0
    m = abs(M)
    L = [0 for x in range(n)]
    i = n-1
    while(m != 0):
        rem = m%2
        m = m//2
        L[i] = rem
        i = i-1
    
    if M<0:
       return twos_comp(L)
   
    return L

def foo(a, n, AQq0):
    l = [0 for x in range(len(AQq0))]
        
    for i in range(0, n):
        l[i] = a[i]
    
    for i in range(n, 2*n):
        l[i] = AQq0[i]
    
    l[2*n] = AQq0[2*n]
    return l   

def SignedBinary2Dec(l):
        a=0
        e=len(l)-1
        if l[0] == 1:
            l3 = twos_comp(l)
        else:
            l3 = l 
            
        for x in l3:
            a = a + (x*(2**e))
            e-=1
            
        if l[0] == 1:
            a = a*-1
        return a
    
def BoothMul(M, Q):
  
    q0 =  [0]
    m = binary(M)
    q = binary(Q)
    a = [0 for x in range(n)]
    minus_m = twos_comp(m)
    AQq0 = a + q + q0
    
    print(f'initially AQq0={AQq0}')
    for x in range(n):
        
        if   (AQq0[(2*n)-1]==1 and AQq0[2*n]==0): #10
            a    = addb(AQq0[0:n], minus_m)
            AQq0 = foo(a, n, AQq0)
        elif (AQq0[(2*n)-1]==0 and AQq0[2*n]==1): #01
            a    = addb(AQq0[0:n], m)
            AQq0 = foo(a, n, AQq0)
        
        AQq0 = arshift(AQq0)
        print(f'n={x} AQq0={AQq0}')
        
    return SignedBinary2Dec(AQq0[0:(2*n)])
    
   

M  =  -3
Q  =  40
n  =  32
print(BoothMul(M, Q))
