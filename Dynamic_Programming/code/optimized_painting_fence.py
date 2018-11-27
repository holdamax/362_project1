# -*- coding: utf-8 -*-
"""
Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color. 


Input: Both n and k are positive integers.
Please write first argument - number of posts, second argumet - number of colors!
"""
def combo(a,b):
    return a**b
def find_combinations(n, c):
    i=3
    if n<=0:
        return 0
    elif n in range(1,i):
        return combo(c,n)
    elif i<=n:
        s=c
        d=s*(c-1)
        for k in range(i,n+1):
            pd=d
            d=(s+d)*(c-1)
            s=pd*1
    return s+d

if __name__=="__main__":
    colours = int(input('How much colors you have? '))
    n = int(input('How much posts you have? '))
    if find_combinations(n, colours)==0:
        print("Okay, Houston, we've had a problem here")
    else:
        print('You have %s ways of painting the fence.' %(find_combinations(n, colours)))