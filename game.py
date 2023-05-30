#Import function using one small game  
import random
x=random.randint(0,10)
while (True):
       y=int(input("guess the anyy number(0-10)>>"))
       if x!=y:
          print("ohh sorry !! Try again!!")
       else:
        print("yuhh be the won the match !!")
        break