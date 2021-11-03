import numpy as np
import matplotlib.pyplot as plt
import math


prices = [500, 300, 200]  # f; possible prices
capacity = 100                      # C; capacity of flight
T = 600              # T; time period; 1 request per period
mu = [0.001, 0.015, 0.05]
v = [0.01, 0.005, 0.0025]

optimal_policy = []



def bellman(x):

    for t in range(T):
        customer = np.random.randint(0,2) # generate a state between 0 and 2
        lambda_i = mu[customer] * math.exp(v[customer]*t) # calculate probability of request depending on class and time (class = customer???)

    pass

