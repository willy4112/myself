# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:22:21 2022

@author: willy
"""

import random

List_number = [0,1,2,3,4,5,6,7,8,9]
Answer = random.sample(List_number,4)

Enter = [int(n) for n in input('請輸入數字，若輸入0表示放棄:')]

a = 0
b = 0
times = 1

while 1==1:
    for i in range(4):
        for j in range(4):
            if Enter[j] == Answer[i] and i==j : a +=1
            if Enter[j] == Answer[i] and i!=j : b +=1
    print(a,'A',b,'B')
        
    if a == 4:
        print('答案為', Answer,'共花了', times,'次')
        break
    Enter = [int(n) for n in input('請輸入數字，若輸入0表示放棄:')]
    if Enter[0] == 0 and len(Enter)==1:
        print('答案為', Answer,'已放棄')
        break
    a = 0
    b = 0
    times += 1
