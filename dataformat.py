# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:06:40 2017

@author: praveena.r
"""
import string
import random
try1=open(r'D:\try1.txt','r',encoding='utf8')
try1=try1.readlines()
try1= list(filter(None, try1))
#try3=[]
#for line in range(len(try1):
 #   try3.append(try1[line].split('.'))
#try1=try1.readlines()
try2=[]
for i in range(len(try1)):
   try2.append(try1[i].split())

w=open(r'D:\for.txt','w+',encoding='utf8')
j=0
while(j<len(try1)):
#for j in range(len(try2)):
    randomWord=random.choice(try2[j])
    temp=(list(randomWord))
    #pretemp=temp
    #pretemp=''.join(pretemp)
    temp[random.choice(range(len(temp)))]=random.choice(string.ascii_letters)
    temp=''.join(temp)
    edited='<del>'+temp+'</del><ins>'+randomWord+'</ins>'
    #for ij in range(len(try2[j])):
    if randomWord in try2[j]:
        k=try2[j].index(randomWord)
        try2[j][k]=edited
        try2[j]=' '.join(try2[j])
        j=j+1        
for line in try2:
    w.write('\n'+line)