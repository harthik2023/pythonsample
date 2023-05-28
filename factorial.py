#Finding the factorial of the numbers
x=int(input("x>> ") )
factorial=1
if x==0:
    print("Factorial of the nuber '0' is ")
elif x==1:
    print("Factorial of the nuber '1' is ")
else:
   for i in range(1,x+1):
     factorial=factorial*i
print(factorial)