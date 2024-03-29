#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)
        
    def test_eval_5 (self) :
        v = collatz_eval(831, 180)
        self.assertEqual(v, 171)

    def test_eval_6 (self) :
        v = collatz_eval(428, 72)
        self.assertEqual(v, 144)

    def test_eval_7 (self) :
        v = collatz_eval(515, 19)
        self.assertEqual(v, 144)

    def test_eval_8 (self) :
        v = collatz_eval(753, 969)
        self.assertEqual(v, 179)
        
    def test_eval_9 (self) :
        v = collatz_eval(324, 871)
        self.assertEqual(v, 179)

    def test_eval_10 (self) :
        v = collatz_eval(170, 735)
        self.assertEqual(v, 171)

    def test_eval_11 (self) :
        v = collatz_eval(309, 902)
        self.assertEqual(v, 179)

    def test_eval_12 (self) :
        v = collatz_eval(928, 201)
        self.assertEqual(v, 179)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      32      1      0      0    97%   78
---------------------------------------------------------
TOTAL            50      1      6      0    98%
"""
