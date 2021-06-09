# -*- coding: utf-8 -*-
"""
CS 351 - Artificial Intelligence 
Assignment 3

Student ID = ma04289
"""

import numpy as np
import matplotlib.pyplot as plt

"""This function takes actual and predicted ratings and compute total mean square error(mse) in observed ratings."""
def computeError(R,predR):
    
    """Your code to calculate MSE goes here"""    
    
    m,n = R.shape
    result = np.zeros((m,n))
    count = 0
    for i in range(m):
        for j in range(n):
            if (R[i][j]):
                result [i][j] = (R[i][j] - predR[i][j])**2
    return np.sum(result) / np.sum(R>0)
    
"""
This fucntion takes P (m*k) and Q(k*n) matrices alongwith user bias (U) and item bias (I) and returns predicted rating. 
where m = No of Users, n = No of items
"""
def getPredictedRatings(P,Q,U,I):

    """Your code to predict ratinngs goes here"""
    m = len(P)
    n  = len(Q[0])
    ans = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            ans[i][j] = np.dot(P[i,:],Q[:,j])+U[i][0]+I[0][j]
    return ans

"""
This fucntion runs gradient descent to minimze error in ratings by adjusting P, Q, U and I matrices based on gradients.
The functions returns a list of (iter,mse) tuple that lists mse in each iteration
"""
def runGradientDescent(R,P,Q,U,I,iterations,alpha):
   
    stats = []
    
    """Your gradient descent code goes here"""    
    m,n = R.shape
    for iter in range(iterations):
        for i in range(m):
            for j in range(n):
                if R[i][j] > 0 :
                    eij = R[i][j] - np.dot(P[i,:],Q[:,j]) - U[i][0] - I[0][j]
                    for ki in range(k):
                        P[i][ki] = P[i][ki]+ alpha * (2 * eij * Q[ki][j])
                        Q[ki][j] = Q[ki][j] + alpha * (2 * eij * P[i][ki])
                    U[i][0] = U[i][0] + 2 * alpha * eij
                    I[0][j] = I[0][j] + 2 * alpha * eij
        predict  = getPredictedRatings(P,Q,U,I)
        mse = computeError(R,predict)
        stats.append((iter,mse))

                  
    """"finally returns (iter,mse) values in a list"""
    return stats
    
""" 
This method applies matrix factorization to predict unobserved values in a rating matrix (R) using gradient descent.
K is number of latent variables and alpha is the learning rate to be used in gradient decent
"""    

def matrixFactorization(R,k,iterations, alpha):

    """
    Your code to initialize P, Q, U and I matrices goes here. P and Q will be randomly initialized whereas U and I will be initialized as zeros. 
    Be careful about the dimension of these matrices
    """
    m,n = R.shape
    #    P = 
    P = np.random.rand(m,k)
    #    Q = 
    Q = np.random.rand(k,n)
    #    U = 
    U = np.zeros((m,1))
    #    I = 
    I = np.zeros((1,n))

    #Run gradient descent to minimize error
    
    stats = runGradientDescent(R,P,Q,U,I,iterations,alpha)
    print('R matrx:')
    print(R)
    print('P matrx:')
    print(P)
    print('Q matrix:')
    print(Q)
    print("User bias:")
    print(U)
    print("Item bias:")
    print(I)
    print("P x Q:")
    print(getPredictedRatings(P,Q,U,I))
    plotGraph(stats)
       
    
def plotGraph(stats):
    i = [i for i,e in stats]
    e = [e for i,e in stats]
    plt.plot(i,e)
    plt.xlabel("Iterations")
    plt.ylabel("Mean Square Error")
    plt.show()    
    
""""
User Item rating matrix given ratings of 5 users for 6 items.
Note: If you want, you can change the underlying data structure and can work with starndard python lists instead of np arrays
We may test with different matrices with varying dimensions and number of latent factors. Make sure your code works fine in those cases.
"""
R = np.array([
[5, 3, 0, 1, 4, 5],
[1, 0, 2, 0, 0, 0],
[3, 1, 0, 5, 1, 3],
[2, 0, 0, 0, 2, 0],
[0, 1, 5, 2, 0, 0],
])

k = 3
alpha = 0.01
iterations = 500

matrixFactorization(R,k,iterations, alpha)
