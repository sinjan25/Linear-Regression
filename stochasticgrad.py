# USING STOCHASTIC GRADIENT DESCENT

import random
import sys
import os

print("Enter number of training examples:")
m=int(sys.stdin.readline())

y=[]
x0=[]
x1=[]
x2=[]

print("Enter area, age and price of house:")

for i in range(0, m):
     p=float(sys.stdin.readline())
     q=float(sys.stdin.readline())
     r=float(sys.stdin.readline())
     x0.append(1)
     x1.append(p)
     x2.append(q)
     y.append(r)

# FEATURE SCALING AND MEAN NORMALIZATION

sumx1=0
sumx2=0

for i in range(0,m):
     sumx1=sumx1+x1[i]
     sumx2=sumx2+x2[i]
     
     
meanx1=sumx1/m;
meanx2=sumx2/m;

rng1=max(x1)-min(x1)
rng2=max(x2)-min(x2)

for i in range(0,m):
     x1[i]=(x1[i]-meanx1)/rng1
     x2[i]=(x2[i]-meanx2)/rng2
     
     
print x0
print x1
print x2
print y

theta0=0
theta1=0
theta2=0
j=0

print("Enter value of alpha:")
alpha=float(sys.stdin.readline())

iter=0

print("Iteration  J(theta)  theta0  theta1  theta2")
while ('true'):
        
        old=j   #old will store value of j for the previos iteration
        j=0
                
        for i in range(0, m):
                theta0=theta0 - alpha*(theta0*x0[i] + theta1*x1[i] + theta2*x2[i] - y[i])
                theta1=theta1 - alpha*(theta0*x0[i] + theta1*x1[i] + theta2*x2[i] - y[i])*x1[i]
                theta2=theta2 - alpha*(theta0*x0[i] + theta1*x1[i] + theta2*x2[i] - y[i])*x2[i]
         
                
        for i in range(0,m):
                j=j+((theta0*x0[i] + theta1*x1[i] + theta2*x2[i] - y[i])**2)/(2*m)          
                
        iter=iter+1
        print(iter,' ',j,' ',theta0,'   ',theta1,' ',theta2,'\n')
        
        if (abs(j-old)<0.0001):
                break
          

print("Final values:\ntheta0=",theta0,"    theta1=",theta1,"     theta2=",theta2)       


print("Enter area and age:")
area=float(sys.stdin.readline())
age=float(sys.stdin.readline())



price=theta0 + theta1*(area-meanx1)/rng1 + theta2*(age-meanx2)/rng2
print("Price:",price)



