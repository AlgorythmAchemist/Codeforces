#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
n,m,a=map(int,input().split())
print(math.ceil(n/a)*math.ceil(m/a))