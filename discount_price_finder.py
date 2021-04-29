print("Hello, input price")
P = int(input())
print("Input discount")
D = int(input())
n = 100-D
g = P*n/100
print("How much is the sales tax in %")
i = int(input())
t = i+100
f = t*g
F = f/100
print("The final price is $", F)