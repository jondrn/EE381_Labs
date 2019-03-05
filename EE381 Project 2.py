# EE 381 Spring 2019 Project 1
# Jonathan Duran
# 014327168
# Start Date:  2/11/2019
# Finish Date: 2/18/2019
# Description: This program will show several simulations using a pseudo-random number generation
#              including tasks such as rolling a die, flipping a coin, and randomly throwing a ball

import math
import time
from collections import Counter


def random():
    s = time.time()
    m = 8601
    a = 4857
    n = 10000
    randomlist = []
    print("RANDOM VALUES")
    for i in range(100):
        s = (s * m + a) % n
        r = s / float(n)
        randomlist.append(r)
    for i in randomlist:
        print("{0:.4f}".format(i))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def coinflip():
    s = time.time()
    m = 8601
    a = 4857
    n = 10000
    heads = []
    tails = []
    print("COIN FLIP")
    for i in range(25):
        s = (s * m + a) % n
        r = s / float(n)
        coin = math.floor(2 * r)
        if coin == 0:
            print("Tails")
            tails.append(coin)
        else:
            print("Heads")
            heads.append(coin)
    print("# of Heads: ", len(heads))
    print("# of Tails: ", len(tails))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def diceroll():
    s = time.time()
    m = 8601
    a = 4857
    n = 10000
    print("DIE ROLL")
    for i in range(25):
        s = (s * m + a) % n
        r = s / float(n)
        die = math.floor(6 * r + 1)
        print(die)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def probability():
    s = time.time()
    m = 8601
    a = 4857
    n = 10000
    iterations = 100000
    prob_list = []
    count = 0
    for x in range(iterations):
        for i in range(3):
            s = (s * m + a) % n
            r = s / float(n)
            prob = math.floor(5 * r + 1)
            prob_list.append(prob)
        prob_list = sorted(prob_list)
        prob_list = Counter(prob_list)
        if len(list(prob_list)) == 3:
            count += 1
        prob_list = []
    full_probability = count / iterations
    print("There are 3 balls and 5 cans. If you were to randomly throw the 3 balls, ")
    print("the probability that they would all land in different cans is", full_probability)


def main():
    random()
    coinflip()
    diceroll()
    probability()
    return 0


main()
