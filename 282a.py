#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=int(input())
x=0
for i in range(0,n):
    stringer = input()
    if '++' in stringer:
        x+=1
    elif '--' in stringer:
        x-=1
print(x)