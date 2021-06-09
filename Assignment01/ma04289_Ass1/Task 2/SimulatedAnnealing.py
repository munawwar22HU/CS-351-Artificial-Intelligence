import math
import random
import matplotlib.pyplot as plt
import numpy as np
def sphere(x,y):
    return x**2+y**2
def rosenbrock(x,y):
    return 100*(x**2 - y**2)+(1-x)**2
def griewank(x,y):
    return (x**2+y**2)/4000  - math.cos(x)*math.cos(y/math.sqrt(2))+1
def RandomNeighbour(x,y,StepSize,Function,Limits):
    x_values = [-StepSize+x,x,x+StepSize]
    y_values = [-StepSize+y,y,y+StepSize]
    Neighbours = []
    for i in x_values:
        for j in y_values:
            if Limits[0]<= i <=Limits[1] and Limits[2] <= j <=Limits[3]:
              
                Neighbours.append((Function(i,j),i,j))
    return Neighbours[random.randint(0,len(Neighbours)-1)]


Solution = list()
values = set()
def SimulatedAnnealing(Function,Limits,Step,IsMax):
    Temp= 1000
    EndTemp = 0.0000000000001
    Alpha = 0.8
    x = random.uniform(Limits[0],Limits[1])
    y = random.uniform(Limits[2],Limits[3])
   
    
    while Temp > EndTemp:
        for i in range(10):
            if IsMax:

                trial = RandomNeighbour(x,y,Step,Function,Limits)
                current = Function(x,y)
                delta = trial[0] - current
                values.add((x,y))
                if delta >0 :
                    x,y = trial[1],trial[2]
                   
                else:
                    m = math.exp(delta/Temp)
                    p = random.uniform(0,1)
                    if p < m:
                        x,y = trial[1],trial[2]
                       
            else:
                current = Function(x,y)
                trial = RandomNeighbour(x,y,Step,Function,Limits)
                delta = trial[0] - current
                values.add((x,y))
                if delta <0 :
                    x,y = trial[1],trial[2]
                    
                else:
                    m = math.exp(-delta/Temp)
                    p = random.uniform(0,1)
                    if p < m:
                        x,y = trial[1],trial[2]
            Solution.append(current)
                        

        Temp = Temp * Alpha
    return (current,x,y)
Limits = [-5,5,-5,5]
val=SimulatedAnnealing(griewank,Limits,0.1,False)
print(val)





x_values = list()
y_values = list()
for x,y in values:
    x_values.append(x)
    y_values.append(y)

# ax[0].plot(Solution,c='Red')
# ax[1].plot(x_values,c='Blue')
# ax[2].plot(y_values,c='Green')

plt.subplot(311)
plt.plot(Solution,c="Red")
plt.ylabel("Objective Function")


plt.subplot(312)
plt.plot(x_values,c="Blue")
plt.ylabel("X-coordinates")


plt.subplot(313)
plt.plot(y_values,c="Green")
plt.ylabel("Y-coordinates")
plt.show()





