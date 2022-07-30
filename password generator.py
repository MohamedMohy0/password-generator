import string
import random
a1=list(string.ascii_lowercase)
a2=list(string.ascii_uppercase)
a3=list(string.digits)
random.shuffle(a1)
random.shuffle(a2)
random.shuffle(a3)
x=int(input("enter the num of the characters:"))
pass1=round(x*(40/100))
pass2=round(x*(20/100))
password=[]
for i in range(pass1):
    password.append(a1[i])
    password.append(a2[i])
for u in range(pass2):
    password.append(a3[i])
random.shuffle(password)
password="".join(password[0:])
print(password)