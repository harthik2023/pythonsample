import base64

def encode():
     x=input("Enter the any encoded  message>>")
     x_in_bytes=bytes(x,"utf-8")
     Encodedx=base64.b64encode(x_in_bytes)
     print(f"{x}:-{Encodedx}")
     
def decode():
     x=input("Enter the any  decoded message>>")
     x_in_bytes=bytes(x,"utf-8")
     Decodedx=base64.b64decode(x_in_bytes)
     print(f"{x}:-{Decodedx}")
     
print("Encode or Decode message using python")
print("1.Encode \n2.Decode")
y=int(input("choose one option like(1/2)>>"))
if y==1:
    encode()
elif y==2:
    decode()
else:
    print("Invalid option. Try again!!")