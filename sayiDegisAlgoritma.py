#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

"""

a  = input("Doğum Ayınız")
b = input("Doğum Yılınız")

print(a)
print(b)

print("değiştir")

a,b = b,a

print(a)
print(b)