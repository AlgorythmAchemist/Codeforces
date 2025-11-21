#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=int(input())
a=0
for i in range (0,n):
    lister = (input().split())
    summer=sum(int(x) for x in lister)
    a+=1 if summer > 1 else 0
print(a)