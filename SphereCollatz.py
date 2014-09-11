#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

CacheDic={}
def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :

    global CacheDic
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    
    

    if i > j:#switch values if j is smaller
        i,j = j,i
    if j//2+1 > i:#use optimization which removes values less than half the larger value
        i = j//2+1
    MaxCycleLength=1
    def CycleCounter(num):#fuction which finds cycle length and if its a new value adds the value and its cycle lenght to a dictionary. if its a value already stored in the dictionary, then cycle length is looked up rather than re calculated. 
        TempNum=num
        CycleLength = 1
        while num > 1:
            if num in CacheDic:
                CycleLength += CacheDic[num]-1
                num = 1
            elif num % 2 == 0:
                num =  num//2
                CycleLength+= 1
            else:
                num = ((num*3)+1)//2
                CycleLength+=2
        CacheDic[TempNum]= CycleLength
        return CycleLength

 
                      
    
    for x in range (i, j+1):#tests the cycle length against the max. if the value is bigger then it is the new max
        tempcount = CycleCounter(x)
        if tempcount>MaxCycleLength:
            MaxCycleLength=tempcount

    return MaxCycleLength#return max
    


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)


import sys


# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
