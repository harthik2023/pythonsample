# Finding the LCM of two numbers.


x=int(input("x>> "))  #Entering the first num.
y=int(input("y>> "))   #Entering the second num.

if x>y:
    high=x
else:
    high=y

while (True):
    if((high%x==0) & (high%y==0)):
        lcm=high
        break
    high+=1
print(f" LCM of {x} and {y} is {lcm}")
