# https://www.acmicpc.net/problem/11332
import math

n = int(input())

for i in range(n):
    result = False
    s,n,t,l = input().split()
    n,t,l= map(int,[n,t,l])

    sec = (10 ** 8)

    if s == "O(N)":
        if n*t <= sec * l:
            result = True
    
    elif s == "O(N^2)":
        if (n ** 2) * t <= sec * l:
            result = True
    
    elif s == "O(N^3)":
        if (n ** 3) * t <= sec * l:
            result = True
    
    elif s == "O(2^N)":
        if (2 ** n) * t <= sec * l:
            result = True
    elif s == "O(N!)":
        if math.factorial(n) * t <= sec * l:
            result = True
    if result:
        print("May Pass.")
    else:
        print("TLE!")