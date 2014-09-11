#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


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
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    
    


    if i > j:
        i,j = j,i
    if j//2+1 > i:
        i = j//2+1
    CacheList=[]
    MaxCycleLength=1
    def CycleCounter(num):
        CycleLength = 1
        while num > 1:
            if num % 2 == 0:
                num =  num//2
                CycleLength+= 1
            else:
                num = ((num*3)+1)//2
                CycleLength+=2
        return CycleLength

    for Cachenum in range (1, 700000):
        CacheList.append([Cachenum, CycleCounter(Cachenum)])

                       
    for num in range (i, j+1):
        if 0<num<700000:
            TempCycle = CacheList[num-1][1]
            if TempCycle>MaxCycleLength:
                MaxCycleLength=TempCycle
        else:
            TempCycle=CycleCounter(num)
            if TempCycle>MaxCycleLength:
                MaxCycleLength=TempCycle
    return MaxCycleLength
            
    


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end of the range, inclusive
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
