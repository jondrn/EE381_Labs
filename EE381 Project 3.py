# EE 381 Spring 2019 Project 3
# Jonathan Duran
# 014327168
# Start Date:  2/27/2019
# Finish Date:
# Description:

import random

# ----------------------------------------------------------------------------------------------------------------------
print("Simulation of Bernoulli Random Variable")
p = float(input("Enter the probability of success: "))
q = int(input("Enter the number of trials: "))
print("\n")
# ----------------------------------------------------------------------------------------------------------------------
print("BERNOULLI RANDOM VARIABLE:")
for j in range(q):
    r = random.uniform(0, 1)
    if r < p:
        print("1", end=" ")
    else:
        print("0", end=" ")
print("\n")
# ----------------------------------------------------------------------------------------------------------------------
l = [] # record position of particle
s = random.randint(0, 1)
l.append(s)
for i in range(25):
    r = random.uniform(0, 1)
    if s == 0 and r < p:
        s = 1
    elif s == 1 and r < q:
        s = 0
    l.append(s)
# ----------------------------------------------------------------------------------------------------------------------
for i in range(25):
    print(l[i], end=" ")
    if i % 10 == 9:
        print()

