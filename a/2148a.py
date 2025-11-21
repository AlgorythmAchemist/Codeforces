#!/usr/bin/env python3
# -*- coding: utf-8 -*-
t=int(input())
for i in range (0,t):
    x,n=map(int, input().split())
    print(0 if n%2 == 0 else x)