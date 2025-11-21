#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=int(input())
for i in range (0,n):
    w=input()
    if len(w)>10:
        print(w[:1]+str(len(w)-2)+w[-1])
    else:
        print(w)
