print("Choose one option of these three options (1/2/3) ")
print("1.square\n2.cube\n3.fourth power")
p=int(input("enter the one option like (1/2/3) ="))
num=int(input("enter the any number ="))
if p==1:
    print(f"square of the {num} is =")
    print(num*num)
elif p==2:
    print(f"cube of the {num} is = ")
    print(num*num*num)
elif p==3:
    print(f"fourth power of the {num} is =")
    print(num*num*num*num)
else:
    print("invalid option. Please try again!!")
